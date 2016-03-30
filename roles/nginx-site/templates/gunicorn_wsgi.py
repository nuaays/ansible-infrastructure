import logging
from {{ nginx_site.name }} import create_app
from werkzeug.contrib.fixers import ProxyFix

# to deploy the database, run `reset_db` and then copy from development location

app = create_app({
    'SECRET_KEY': '{{ nginx_site.key }}',
    'SQLALCHEMY_DATABASE_URI': 'sqlite:////var/lib/sqlite/{{ nginx_site.name }}.db',
    'DEBUG': False
})

for logger in [app.logger, logging.getLogger('sqlalchemy')]:
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.ERROR)

app.wsgi_app = ProxyFix(app.wsgi_app)
