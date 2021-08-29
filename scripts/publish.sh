#!/bin/bash
cd $(dirname $0)/..

./scripts/test && \
poetry build

if [[ $? != 0 ]]; then
  exit 1
fi

if [[ $1 == "--production" || $1 == -p ]]; then
  poetry publish
else
  poetry publish -r testpypi
fi
