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

DEFAULT_LANG = 'fr'

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

PLUGIN_PATHS = ['plugins', os.path.expanduser('~/pelican-plugins')]
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

RESUME = get_data('en')

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

# STATIC_PATHS = ['theme/static']
"""
EDUCATIONS = [
    {
        'degree': 'Physics Engineer, specialisation in Micro-Nano-electronics',
        'meta': 'Grenoble INP Phelma',
        'time': '2009'
    },
    {
        'degree': 'Year in Exchange',
        'meta': 'UCSD San Diego',
        'time': '2008-2009'
    },
    {
        'degree': 'High School, Baccalauréat S mention Bien',
        'meta': 'Lycée Général Loudéac',
        'time': '2004'
    }
]

LANGUAGES = [
    {
        'name': 'French',
        'description': 'Native'
    },
    {
        'name': 'English',
        'description': 'Fluent'
    }
]
INTERESTS = [
    'Laser cutting',
    'Programming, ever since my dad got a 286 in the 90s'
]
PROJECTS = [
    {
        'title': 'Open Source Contributions',
        'tagline': 'Contributor to various projects: FlatCAM, openapi-generator, pulumi'
    },
    {
        'title': 'API-access libraries',
        'tagline': 'Bridge API, Budget Insight, Fintecture, Rebrickable'
    }
]
PROJECT_INTRO = 'Projects or Open-Source libraries'
SKILLS = [
    {
        'title': 'Python',
        'details': 'creating CLI-tools, backend APIs, one-off scripts, scraping, etc...'
    },
    {
        'title': 'Sysadmin - Devops',
        'details': 'Maintained multiple servers, personal & work, heavily using '
                   'Docker containers, using IaC (terraform, pulumi), interested in kubernetes'
    },
    {
        'title': 'Javascript',
        'details': 'Modified & maintained Vue.js site & various js code'
    },
    {
        'title': 'Java',
        'details': 'Modified & maintained API services in Servlent/OSGI \n Minecraft modding'
    },
]
CAREER_SUMMARY = [
    'Multi-faceted Engineer, from the electrons to the Cloud',
    '<i class="fa fa-heart"></i> building projects, and helping others build their projects']

TAGLINE = 'Lead Full Stack Developer'

"""
