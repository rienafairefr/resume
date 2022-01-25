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
            "graphql": open('themes/resume/static/images/graphql.svg').read().replace('<svg', '<svg width=45'),
            "openapi": open('themes/resume/static/images/openapi.svg').read().replace('<svg', '<svg width=45'),
            "terraform": open('themes/resume/static/images/terraform.svg').read().replace('<svg', '<svg width=45'),
            "pulumi": open('themes/resume/static/images/pulumi.svg').read().replace('<svg', '<svg width=45'),
            "open-source": open('themes/resume/static/images/open-source.svg').read().replace('<svg', '<svg width=45')
        }


def get_data(lang):
    with open(os.path.join('data', lang, 'resume.json'), 'r') as resume_file:
        resume = json.load(resume_file)
        if 'email' in resume['basics']:
            resume['basics']['email'] = obfuscate_string(resume['basics']['email'])
        if resume['basics']['x-emails']:
            _emails = []
            for e in resume['basics']['x-emails']:
                if isinstance(e, dict):
                    _emails.append({ **e, "email": obfuscate_string(e['email']) })
                else:
                    _emails.append(obfuscate_string(e))
            resume['basics']['x-emails'] = _emails
        resume['basics']['phone'] = obfuscate_string(resume['basics']['phone'])
        def get_wordmark(w):
            if w in ['javascript', 'd3js', 'linux', 'php', 'flutter']:
                return False
            
            return True
        for key in 'work', 'projects', 'skills':
            kc = f"{key}_by_category"
            resume[kc] = {}
            for item in resume.get(key, []):
                if 'x-category' in item:
                    resume[kc].setdefault(item['x-category'], []).append(item)
                if 'x-stack' in item:
                    item['x-stack'] = [
                        {
                            "icon": ICONS.get(stack, f"<i class =\"devicon-{stack}-plain{'-wordmark' if get_wordmark(stack) else ''}\"></i>")
                        } for stack in
                        item['x-stack']
                    ]
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
