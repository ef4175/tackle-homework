#!/usr/bin/env bash

DOCKER_BUILDKIT=1 docker build -t tackle-app tackle-app
docker run -it \
  -p 3000:3000 \
  --rm \
  tackle-app yarn start
