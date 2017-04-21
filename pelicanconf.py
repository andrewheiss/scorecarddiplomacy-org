#!/usr/bin/env python3

# ------------------
# Site information
# ------------------
AUTHOR = 'Judith Kelley'
SITENAME = 'Scorecard Diplomacy'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DEFAULT_LANG = 'en'

TYPOGRIFY = True  # Nice typographic things
TYPOGRIFY_IGNORE_TAGS = ['h1']


# ---------------
# Site building
# ---------------
DELETE_OUTPUT_DIRECTORY = True

# Theme
THEME = 'theme'

# Folder where everything lives
PATH = 'content'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

STATIC_PATHS = ['.htaccess', 'favicon.ico', 'robots.txt', 'files']
READERS = {'html': None}  # Don't parse HTML files

# No feeds
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# None of these pages
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
TAGS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''


# ------------
# Site items
# ------------
MENUITEMS = [('About', '/about/'),
             ('Author', '/author/'),
             ('Press', '/press/'),
             ('Case studies', '/case-studies/'),
             ('Data', '/data/'),
             ('Survey', '/survey/'),
             ('Human trafficking', '/human-trafficking/')]

CASES = [('Case studies', '/case-studies/'),
         ('Case selection and methodology', '/case-studies/case-selection/'),
         ('Argentina', '/case-studies/argentina/'),
         ('Armenia', '/case-studies/armenia/'),
         ('Chad', '/case-studies/chad/'),
         ('Ecuador', '/case-studies/ecuador/'),
         ('Honduras', '/case-studies/honduras/'),
         ('Indonesia', '/case-studies/indonesia/'),
         ('Israel', '/case-studies/israel/'),
         ('Japan', '/case-studies/japan/'),
         ('Kazakhstan', '/case-studies/kazakhstan/'),
         ('Malaysia', '/case-studies/malaysia/'),
         ('Mozambique', '/case-studies/mozambique/'),
         ('Nigeria', '/case-studies/nigeria/'),
         ('Oman', '/case-studies/oman/'),
         ('United Arab Emirates', '/case-studies/united-arab-emirates/'),
         ('Zimbabwe', '/case-studies/zimbabwe/')]

SURVEY_MENU = [('Survey', '/survey/'),
               ('Survey methods', '/survey/methods/'),
               ('Survey data', '/survey/data/'),
               ('“From the Trenches” article', '/survey/article/'),
               ('Report for NGOs', '/survey/ngo-report/'),
               ('Raw summary', '/survey/summary-raw/'),
               ('Original survey', '/survey/original-survey/'),
               ('Survey invitation', '/survey/invitation/')]

DATA_MENU = [('Data', '/data/'),
             ('Methods appendix', '/data/methods-appendix/'),
             ('Statistical analysis and data', '/data/statistics-data/'),
             ('Additional analysis', '/data/additional-analysis/'),
             ('Content analysis', '/data/content-analysis/')]

DEFAULT_PAGINATION = False

PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican-bootstrapify']

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.smarty': {},
        'markdown.extensions.extra': {},
        'markdown.extensions.footnotes': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {},
        'markdown.extensions.codehilite': {'css_class': 'codehilite'},
        'markdown.extensions.headerid': {'level': 1}
    },
    'output_format': 'html5',
}


# ---------------
# Jinja filters
# ---------------
import jinja2
import os

# Get the final basename or directory name of a path
def get_slug(url):
    slug = os.path.basename(os.path.dirname(url))
    return slug

JINJA_FILTERS = {'get_slug': get_slug}
