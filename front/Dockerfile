# develop stage
FROM node:12.1-alpine as develop-stage
WORKDIR /usr/src/app
COPY package.json ./
RUN yarn install
COPY . .
# build stage
FROM develop-stage as build-stage
RUN yarn build
# production stage
FROM nginx:1.15.7-alpine as production-stage
COPY --from=build-stage /usr/src/app/dist /usr/share/nginx/html
RUN yarn build
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]