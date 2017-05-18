#!/bin/bash
set -ev

export SKIP_ENV_CHECK=1

flake8 {{cookiecutter.app_name}} tests
pytest --cov={{cookiecutter.app_name}}
flask-resty-swagger {{cookiecutter.app_name}} > docs.json
