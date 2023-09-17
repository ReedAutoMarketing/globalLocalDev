# Use a Node base image to build the React app
FROM node:14 as build

WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application
COPY . ./

# Build the React app
RUN npm run build

# Use an Nginx base image to serve the React app
FROM nginx:alpine

# Copy the build folder from the previous stage to the nginx html directory
COPY --from=build /app/build /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]