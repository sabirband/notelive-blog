AUTHOR = 'Sabir'
SITENAME = 'NOTELIVE'
SITEURL = 'https://blog.notelive-shvalyuk.com'
SITESUBTITLE = 'Юридичний блог майбутнього: Цифрова грамотність, Спадщина, Майбутнє.'
SITETITLE = 'ТЕСТОВЫЙ ЗАГОЛОВОК NOTELIVE'
PATH = "content"

TIMEZONE = 'Europe/Kyiv'

DEFAULT_LANG = 'uk'
OUTPUT_PATH = 'output/'

THEME = 'themes/Flex'
# publishconf.py

# ... (інші імпорти та налаштування, успадковані з pelicanconf - залишаються) ...

JINJA_ENVIRONMENT = {
    'extensions': [
        'jinja2.ext.loopcontrols',
    ]
}

# ... (STATIC_PATHS, EXTRA_PATH_METADATA та інші налаштування publishconf.py - залишаються) ...


PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap', 'neighbors', 'related_posts']
STATIC_PATHS = ['images', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
SITELOGO_TEXT = 'Notelive'
SITELOGO_TEXT_COLOR = '#FFD700'
SITEMENU = [('Розлучення', '/розлучення.html'), ('Аліменти', '/аліменти.html'), ('Спадщина', '/спадщина.html'), ('Шлюб', '/шлюб.html'), ('Цифрові активи', '/цифрові-активи.html'), ('Бізнес і родина', '/бізнес-і-родина.html'), ('Криптоправо', '/криптоправо.html'), ('Право майбутнього', '/право-майбутнього.html'), ('Юридична гігієна', '/юридична-гігієна.html'), ('Форма', '/форма.html'), ('Звернутись', 'https://notelive.ua')]
THEME_COLOR = '#000000'
THEME_TEXT_COLOR = '#000000'
THEME_ACCENT_COLOR = '#FFD700'
SUMMARY_MAX_LENGTH = 40


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
