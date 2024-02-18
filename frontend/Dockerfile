# Use the official Node.js image as base
FROM node:16-alpine AS build

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json to install dependencies
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the entire project directory to the container
COPY . .

# Build the React app
RUN npm run build

# Use NGINX image as base for serving the React app
FROM nginx:alpine

# Copy build files from the previous stage to NGINX directory
COPY --from=build /app/build /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start NGINX server
CMD ["nginx", "-g", "daemon off;"]
