### Stage 1: build ###

FROM node:latest as builder

# Set working directory.
RUN mkdir /app
WORKDIR /app

# Copy app dependencies.
COPY frontend/package.json frontend/package-lock.json /app/frontend/

# Install app dependencies.
RUN npm install --prefix frontend

# Copy app files.
COPY . /app

# Default build configuration.
ARG configuration=production

# Build app
RUN npm run build --prefix frontend -- --output-path=./dist/out --configuration $configuration


### Stage 2: delivery ###

FROM nginx:1.15.7-alpine

# Remove default nginx website
RUN rm -rf /usr/share/nginx/html/*

# Copy output directory from builder to nginx image.
COPY --from=builder /app/frontend/dist/out /usr/share/nginx/html

# Copy nginx configuration file.
COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf