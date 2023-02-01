# Create a React Project

```
npx create-react-app frontend
```

# Get into React project folder
```
cd frontend
```
# Test the React project and build it

> runs test

```
npm run test
```
› Press q to quit watch mode 

> builds a production version of the application

```
npm run build
```

** Note **

> starts up a development server. don't use this for production

```
npm run start
```

# Inside the react project folder create a new Dockerfile with a custom name Dockerfile.dev
```
nano Dockerfile.dev
```
> this is only for the dev environment as its going to contain npm run start, which is development server command
> the server docker file is just Dockerfile which is going to have the command npm run build

```
# base image

FROM node:16-alpine

# /app will be created if it doesnt exist. also will be set as the default directory
WORKDIR "/app"

# copy package.json from the local project folder to the work dir, which is /app
# we are copying package.json initially because to prevent unnecessary downloads
# of node dependencies if there is a change to the source code

COPY package.json .

# install the contents of package.json
RUN npm install

# copy rest of the files
COPY . .


# default startup command for development server
CMD ["npm","run","start"]


```

# Build the image using the custom Dockerfile.dev

```
docker build -f Dockerfile.dev . 
```

# Start the image that you have created

> run docker images to get the image id
```
docker images
```
> run the below command to run the image as a container in docker
```
docker run -p <port_that_docker_exposes_to_outside_world_this_can_be_any_port>>:<application_port_within_docker_container> <image_id>
```
> ex. docker run -p 3000:3000 cc533ea96fb1

## run the image with volume

```
 docker run -p 3000:3000 -v /app/node_modules -v $(pwd):/app cc533ea96fb1
```
>  -v /app/node_modules  --> means use the /app/node_modules within the container as it is, dont mess with it.

>  -v $(pwd):/app       --> means use/map the content of pwd(present working directory) of local system to the /app directory of the container


# Using Docker Compose

> docker-compose.yml

```
version: "3"
services:
  web:
    build:
      context: .
      dockerfile: Dockerfile.dev
    ports:
      - "3000:3000"
    volumes:
      - /app/node_modules
      - .:/app

```
> - /app/node_modules --> means dont refer anything for the /app/node_modules within the container

> - .:/app            --> means refer the current folder in your local machine to the /app folder of the container


> docker compose up

