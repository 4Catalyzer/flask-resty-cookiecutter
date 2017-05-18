# {{cookiecutter.app_name}}

## Before you start

Pin the requirements by running `pip-compile` (requires `pip-tools`)

## Run Locally

- add required environment variables
- `./run.sh`

## Test

- make sure you have a database available at `postgresql://localhost/test`
- `pip install -r requirements.txt && pip install -r requirements-dev.txt`
- `./test.sh`

## Build

- `docker build -t {{cookiecutter.app_name}} .`
