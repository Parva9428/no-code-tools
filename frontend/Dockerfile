FROM node:18-alpine

WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy source code
COPY . .

# Build the app
RUN npm run build

EXPOSE 3000

# Start the app in development mode
ENV NODE_ENV=development
CMD ["npm", "run", "dev"]
