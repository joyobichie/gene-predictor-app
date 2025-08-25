# Start with a Node.js image
FROM node:16-alpine

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json to leverage Docker cache
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of your application source code
COPY . .

# Expose the port Vite will run on
EXPOSE 5173

# The command to start the Vite development server
# '--host' makes it accessible from outside the container
CMD ["npm", "run", "dev"]