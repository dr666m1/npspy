#!/bin/bash
cd $(dirname $0)/..

poetry run black --check . && \
poetry run flake8 && \
poetry run mypy npspy/**.py --strict && \
poetry run pytest
