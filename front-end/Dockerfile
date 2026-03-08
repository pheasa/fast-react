FROM node:25-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install -g npm@11.11.0
RUN npm install

COPY . .

# CMD ["npm", "run", "dev"]
CMD ["npm", "start"]