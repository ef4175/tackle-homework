#!/usr/bin/env bash

DOCKER_BUILDKIT=1 docker build -t tackle-api tackle-api
docker run -it \
  --name tackle-api \
  --rm \
  tackle-api \
  pytest -v functional_tests
