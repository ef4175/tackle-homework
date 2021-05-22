FROM node:16.0.0

USER node
WORKDIR /app

COPY package.json .
COPY yarn.lock .
RUN yarn install

COPY public public
COPY src src
COPY .env .

ENV HOST 0.0.0.0
