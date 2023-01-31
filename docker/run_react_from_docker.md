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
