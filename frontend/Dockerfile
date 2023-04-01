FROM node:16-alpine

WORKDIR /app/frontend/

COPY package*.json /app/frontend/
RUN npm install

COPY . /app/frontend/

CMD ["npm", "start"]

#Starting with a base image, it will set the working directory to /app/frontend where our code shall reside.
#Copy package.json and package-lock.json files to working directory.
#Install all the dependencies.
#Copy our code content to the working directory.
#Set server starting command with CMD