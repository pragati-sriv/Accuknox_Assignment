# Use an official Ubuntu runtime as a parent image
FROM ubuntu:latest

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Make the shell script executable
RUN chmod +x wisecow.sh

# Run the shell script
CMD ["./wisecow.sh"]
