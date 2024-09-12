#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import json
import os
import sys

sys.path.append(os.path.dirname(__file__))

from utils import obfuscate_string

AUTHOR = 'Matthieu Berthomé'
SITENAME = 'Matthieu Berthomé'
SITEURL = ''

PATH = '.'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
THEME = "./themes/resume"

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
    ('You can modify those links in your config file', '#'),
)

# Social widget
SOCIAL = (
    ('You can add links in your config file', '#'),
    ('Another social link', '#'),
)

DEFAULT_PAGINATION = False
DEBUG = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

PLUGIN_PATHS = [os.path.expanduser('~/pelican-plugins')]
PLUGINS = ['i18n_subsites']

ICONS = {
    "graphql": open('themes/resume/static/images/graphql.svg').read(),
    "openapi": open('themes/resume/static/images/openapi.svg').read(),
    "sql": open('themes/resume/static/images/sql.svg').read(),
    "terraform": open('themes/resume/static/images/terraform.svg').read(),
    "pulumi": open('themes/resume/static/images/pulumi.svg').read(),
    "linux": open('themes/resume/static/images/linux.svg').read(),
    "open-source": open('themes/resume/static/images/open-source.svg').read()
}


def get_icon(name, width=None, height=None):
    icon = ICONS.get(name)
    if name in ICONS:
        if width is not None:
            return icon.replace('<svg', f'<svg width={width}')
        elif height is not None:
            return icon.replace('<svg', f'<svg height={height}')


def get_data(lang):
    resume_ = os.path.join('data', lang, 'resume.json')
    if not os.path.exists(resume_):
        return {}
    with open(resume_, 'r') as resume_file:
        resume = json.load(resume_file)
        if 'email' in resume['basics']:
            resume['basics']['email'] = obfuscate_string(resume['basics']['email'])
        if resume['basics']['x-emails']:
            _emails = []
            for e in resume['basics']['x-emails']:
                if isinstance(e, dict):
                    _emails.append({**e, "email": obfuscate_string(e['email'])})
                else:
                    _emails.append(obfuscate_string(e))
            resume['basics']['x-emails'] = _emails
        resume['basics']['phone'] = obfuscate_string(resume['basics']['phone'])

        for key in 'work', 'projects':
            kc = f"{key}_by_category"
            resume[kc] = {}
            for item in resume.get(key, []):
                if 'x-category' in item:
                    resume[kc].setdefault(item['x-category'], []).append(item)
                if 'x-stack' in item:
                    def get_wordmark(w):
                        if w in ('d3js', 'python', 'javascript'):
                            return False
                        return True

                    for i, stack in enumerate(item['x-stack']):
                        stack2 = stack.replace('.', '').lower()
                        stack_icon = get_icon(stack2, height=45)
                        if stack_icon is None:
                            wm = '-wordmark' if get_wordmark(stack2) else ''
                            stack_icon = f'<i style="font-size: 45px;" class="devicon-{stack2}-plain{wm}"></i>'
                        item['x-stack'][i] = {
                            "icon": stack_icon,
                            "name": stack
                        }

        def get_wordmark_skill(w):
            if w in ('d3js', 'python', 'javascript', 'php', 'sql'):
                return False
            return True
        for item in resume['skills']:
            stack2 = item['x-icon']
            stack_icon = get_icon(item['x-icon'], height=32)
            if stack_icon is None:
                wm = '-wordmark' if get_wordmark_skill(stack2) else ''
                stack_icon = f'<i style="font-size: 32px;" class="devicon-{stack2}-plain{wm}"></i>'
            item['x-icon'] = {
                "icon": stack_icon,
                "name": stack
            }

        return resume


I18N_SUBSITES = {
    'en': {
        'OUTPUT_PATH': 'output/en/',
        'THEME': './themes/resume',
        'RESUME': get_data('en')
    },
    'fr': {
        'OUTPUT_PATH': 'output/fr/',
        'THEME': './themes/resume',
        'RESUME': get_data('fr')
    }
}

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n']
}
I18N_GETTEXT_NEWSTYLE = True

RESUME = get_data('en')

PROJECT_INTRO = "<span lang=\"en\">Open-source contributions</span><span lang=\"fr\">Contributions open-source</span>"

######
#
#   RESUME DATA
#
######

CSS_FILE = 'main.css'

PIC = 'profile.png'
