# -*- coding: utf-8 -*-

import os
import shutil
import sys
import datetime

from pathlib import Path
from invoke import task, Collection
from pelican.server import ComplexHTTPRequestHandler, RootedHTTPServer
from pelican.settings import DEFAULT_CONFIG, get_settings_from_file

SETTINGS_FILE_BASE = 'pelicanconf.py'
SETTINGS = {}
SETTINGS.update(DEFAULT_CONFIG)
LOCAL_SETTINGS = get_settings_from_file(SETTINGS_FILE_BASE)
SETTINGS.update(LOCAL_SETTINGS)

CONFIG = {
    'settings_base': SETTINGS_FILE_BASE,
    'settings_publish': 'publishconf.py',
    # Output path. Can be absolute or relative to tasks.py. Default: 'output'
    'deploy_path': SETTINGS['OUTPUT_PATH'],
    'input_path': SETTINGS['PATH'],
    # Github Pages configuration
    'github_pages_branch': 'gh-pages',
    'commit_message': "'Publish site on {}'".format(datetime.date.today().isoformat()),
    # Port for `serve`
    'port': 8000,
    'debug': SETTINGS['DEBUG'],
}


@task
def clean(c):
    """Remove generated files"""
    if os.path.isdir(CONFIG['deploy_path']):
        shutil.rmtree(CONFIG['deploy_path'])
        os.makedirs(CONFIG['deploy_path'])


@task
def build(c):
    """Build local version of site"""
    c.run('pelican {input_path} -s {settings_base} -o {deploy_path} -D'.format(**CONFIG), echo=True)


@task
def rebuild(c):
    """`build` with the delete switch"""
    c.run('pelican {input_path} -d -s {settings_base} -o {deploy_path} -D'.format(**CONFIG), echo=True)


@task
def regenerate(c):
    """Automatically regenerate site upon file modification"""
    c.run('pelican {input_path} -r -s {settings_base} -o {deploy_path} -D'.format(**CONFIG), echo=True)


@task
def serve(c):
    """Serve site at http://localhost:$PORT/ (default port is 8000)"""

    class AddressReuseTCPServer(RootedHTTPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(
        CONFIG['deploy_path'],
        ('', CONFIG['port']),
        ComplexHTTPRequestHandler)

    sys.stderr.write('Serving on port {port} ...\n'.format(**CONFIG))
    server.serve_forever()


@task
def preview(c):
    """Build production version of site"""
    c.run('pelican {input_path} -s {settings_publish} -o {deploy_path}'.format(**CONFIG), echo=True)


@task
def livereload(c):
    """Automatically reload browser tab upon file modification."""
    from livereload import Server
    build(c)
    server = Server()
    # Watch the base settings file
    server.watch(CONFIG['settings_base'], lambda: build(c))
    # Watch content source files
    content_file_extensions = ['.md', '.rst']
    for extension in content_file_extensions:
        content_blob = '{0}/**/*{1}'.format(SETTINGS['PATH'], extension)
        server.watch(content_blob, lambda: build(c))
    # Watch the theme's templates and static assets
    theme_path = SETTINGS['THEME']
    for path in Path(theme_path).rglob('*.*'):
        server.watch(str(path), lambda: build(c))
    # Watch data path
    for path in Path('data').rglob('*.*'):
        server.watch(str(path), lambda: build(c))
    # Serve output path on configured port
    server.serve(port=CONFIG['port'], root=CONFIG['deploy_path'], debug=SETTINGS.get('DEBUG', False))


@task
def gh_pages(c):
    """Publish to GitHub Pages"""
    preview(c)
    c.run('ghp-import -b {github_pages_branch} '
          '-m {commit_message} '
          '{deploy_path} -p'.format(**CONFIG))
