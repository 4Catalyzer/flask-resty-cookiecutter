from collections import defaultdict
import os

from cryptography.hazmat.backends import default_backend
from cryptography.x509 import load_pem_x509_certificate

# -----------------------------------------------------------------------------


def load_certificate(key):
    if key.startswith('-----BEGIN CERTIFICATE-----'):
        cert = load_pem_x509_certificate(key.encode(), default_backend())
        return cert.public_key()

    return key

# -----------------------------------------------------------------------------


ENV_PREFIX = '{{cookiecutter.env_prefix}}'

# when SKIP_ENV_CHECK is set, don't fail if the env variables are not set.
# This is useful when importing the app code without failing
config = defaultdict(str) if os.environ.get('SKIP_ENV_CHECK') else dict()
config.update({
    key.replace(ENV_PREFIX.format(), ''): val
    for key, val in os.environ.items() if key.startswith(ENV_PREFIX)
})

config['BASE_DIR'] = os.path.dirname(
    os.path.dirname(os.path.dirname(__file__)),
)

config['SQLALCHEMY_DATABASE_URI'] = config['DB_URL']
config['DB_SCHEMA'] = '{{cookiecutter.db_schema}}'

# TODO: Remove once this is the default
config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

config['RESTY_JWT_DECODE_ALGORITHMS'] = ['RS256']
config['RESTY_JWT_DECODE_LEEWAY'] = 1
config['RESTY_JWT_DECODE_AUDIENCE'] = config['JWT_DECODE_AUDIENCE']
config['RESTY_JWT_DECODE_ISSUER'] = config['JWT_DECODE_ISSUER']
config['RESTY_JWT_DECODE_KEY'] = load_certificate(config['JWT_DECODE_KEY'])
