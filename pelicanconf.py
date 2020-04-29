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

PATH = 'content'

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


def get_data(lang):
    with open(os.path.join('data', lang, 'resume.json'), 'r') as resume:
        return json.load(resume)


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
RESUME['basics']['email'] = obfuscate_string(RESUME['basics']['email'])
RESUME['basics']['phone'] = obfuscate_string(RESUME['basics']['phone'])
######
#
#   RESUME DATA
#
######

CSS_FILE = 'main-6.css'

PIC = 'profile.png'
