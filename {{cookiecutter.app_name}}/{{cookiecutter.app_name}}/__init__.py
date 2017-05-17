import click
from flask import Flask

from .config import config

# -----------------------------------------------------------------------------

app = Flask('{{cookiecutter.app_name}}')
app.config.from_mapping(config)

if not app.debug:
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

# -----------------------------------------------------------------------------

from . import routes  # noqa

# -----------------------------------------------------------------------------


@app.cli.command()
def initdb():  # pragma: no cover
    from .models import db

    click.echo("initializing database")
    db.create_all()
