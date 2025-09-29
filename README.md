# Weather Application

## Overview
This application provides real-time weather information. Users can query weather conditions for different locations worldwide.

## Features
- Real-time weather updates.
- Search by city
- Simple and intuitive interface.

## Running the Application in a Container

To run the application in a Docker container, follow these steps:

### Prerequisites
- Docker installed on your system.

### Steps
1. **Build the Docker Image**
   
   Navigate to the project directory and build the image using the following command:

    ```bash
    docker build -t weather-app .
    ```

2. **Run the Container**

    After building the image, run the application by starting a container with the following command:

    ```bash
    docker run -d -p 5000:5000 weather-app
    ```
    
    This command runs the application in a detached mode, mapping port 5000 of the container to port 5000 on your host.

3. **Accessing the Application**

    Open a web browser and navigate to `http://localhost:5000` to access the application.

## Contribution

Feel free to contribute to the project by submitting a pull request or opening an issue.

## Versions 

Python 3.12