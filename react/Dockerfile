FROM node:20-alpine AS build
WORKDIR /react

COPY package.json ./
RUN npm install

COPY . .

RUN npm rebuild esbuild

EXPOSE 5173

CMD ["npm", "run", "dev"]
