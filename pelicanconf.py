#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Joshua Gauthier'
SITENAME = u'zwned.info'
SITESUBTITLE = u'$ cat /dev/urandom >> /dev/blog'
SITEURL = 'http://www.zwned.info'

PATH = 'content'

TIMEZONE = 'EST5EDT'

DEFAULT_LANG = u'en'

STATIC_PATHS = ['images','extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

THEME = 'pelican-themes/blueidea'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = []
MENUITEMS = (('Home', 'http://zwned.info'),('Resume', 'http://zwned.info/resume'),)

DISPLAY_CATEGORIES_ON_MENU = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'


YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/index.html'
DAY_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/index.html'

ARCHIVES_SAVE_AS = 'blog/index.html'

RELATIVE_URLS = False

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = (('@zwned', 'https://twitter.com/zwned'),
        ('GitHub', 'https://github.com/zwned'),)

DEFAULT_PAGINATION = 10
