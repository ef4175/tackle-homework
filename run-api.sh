#!/usr/bin/env bash

DOCKER_BUILDKIT=1 docker build -t tackle-api tackle-api
docker run -it \
  -p 5000:5000 \
  --rm \
  tackle-api \
  bash -c "python -c 'import util; util.build_or_refresh_db();' && \
    flask run --host=0.0.0.0"
