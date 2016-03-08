#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Meghann Agarwal'
SITENAME = u"Meghann Agarwal's Blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),)
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('GitHub', 'https://github.com/mepa'),)
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = './themes/pelican-bootstrap3'
#THEME = './themes/pelican-elegant'

#MARKUP = ('md', 'ipynb')


PLUGIN_PATHS = ['./plugins']
#PLUGINS = ['ipynb']

#PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook']

NOTEBOOK_DIR ='notebooks'
