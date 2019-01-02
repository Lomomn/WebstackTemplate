FROM node:8-stretch

WORKDIR /frontend
COPY package*.json /frontend/
COPY yarn.lock /frontend/
RUN yarn install

ENV NODE_ENV=development

COPY . /frontend/
CMD ["npm", "run", "dev"]