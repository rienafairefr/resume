#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from utils import obfuscate_string

AUTHOR = 'Matthieu Berthomé'
SITENAME = 'Matthieu Berthomé'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
THEME = "./themes/resume"

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False
DEBUG = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


######
#
#   RESUME DATA
#
######

CSS_FILE = 'main-6.css'
NAME = 'Matthieu Berthomé'
PIC = 'profile.png'
EMAIL = obfuscate_string('matthieu@mmea.fr')
PHONE = obfuscate_string('(+33) 6 09 63 43 87')
LINKEDIN = 'matthieu-berthomé'
GITHUB = 'rienafairefr'
TWITTER = 'm_berthome'


STATIC_PATHS = ['theme/static']

from en_data import *