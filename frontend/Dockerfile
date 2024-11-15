FROM node:18

WORKDIR /app

# Install dependencies
COPY package.json .
RUN npm install

# Copy application files
COPY . .

# Build the frontend
RUN npm run build

# Serve the app
CMD ["npm", "run", "serve"]
