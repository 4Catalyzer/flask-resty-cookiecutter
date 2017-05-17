#!/bin/sh

export FLASK_APP={{cookiecutter.app_name}}/__init__.py
export FLASK_DEBUG=1

flask run -p 8000
