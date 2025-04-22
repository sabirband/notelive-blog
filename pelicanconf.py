AUTHOR = 'Sabir'
SITENAME = 'NOTELIVE | Юридичний блог майбутнього'
SITEURL = 'https://blog.notelive-shvalyuk.com'
SITESUBTITLE = 'Цифрова грамотність. Спадщина. Майбутнє.'
PATH = "content"
THEME = 'themes/pelican-themes/Flex'
TIMEZONE = 'Europe/Kyiv'

DEFAULT_LANG = 'uk'
OUTPUT_PATH = 'output/'

ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'

DEFAULT_PAGINATION = 10
RELATIVE_URLS = False

CATEGORY_SAVE_AS = ''
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
