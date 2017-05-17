import pytest

from {{cookiecutter.app_name}} import app
from {{cookiecutter.app_name}}.models import db

from .client import AuthorizedClient
from . import mock_data


# -----------------------------------------------------------------------------


@pytest.fixture(scope="session")
def test_app():
    app.config['TESTING'] = True

    app.test_client_class = AuthorizedClient

    return app


@pytest.fixture(scope="session")
def clean_db():
    assert 'test' in str(db.engine.url)

    db.engine.execute('''
        CREATE EXTENSION IF NOT EXISTS pgcrypto;
        DROP SCHEMA IF EXISTS {schema} CASCADE;
        CREATE SCHEMA {schema};
    '''.format(schema=db.metadata.schema))


@pytest.yield_fixture(autouse=True)
def populate_db(clean_db):
    mock_data.populate()
    yield
    mock_data.clear()


@pytest.fixture
def client(test_app):
    return test_app.test_client()


@pytest.fixture(autouse=True)
def config(test_app):
    test_app.config.update({
        'SQLALCHEMY_DATABASE_URI': 'postgresql://localhost/test',
        'RESTY_JWT_DECODE_ALGORITHMS': ['HS256'],
        'RESTY_JWT_DECODE_AUDIENCE': 'audience',
        'RESTY_JWT_DECODE_ISSUER': 'issuer',
        'RESTY_JWT_DECODE_KEY': 'secret',
    })
