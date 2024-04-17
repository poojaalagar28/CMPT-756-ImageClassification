# Image Classification App 🖼️🔍

This application allows you to classify images using state-of-the-art deep learning models. Upload an image and the app will predict the most likely labels for the image!

## How it works

1. **Upload Image**: Upload an image file (JPEG, JPG, or PNG) that you want to classify.
2. **Image Classification**: The app will use the RESNET50 model to predict the labels for the uploaded image.
3. **Display Results**: The top predicted labels along with their confidence scores are displayed, along with the image.

## How to use

### Running the app locally

1. Clone this repository to your local machine. 🖥️
2. Navigate to the project directory in your terminal.
3. Install the required dependencies by running: `pip install -r requirements.txt`. 🛠️
4. Run the Python Flask app using the command: `flask run frontend.py`. 🏃 (CHANGE THIS)
5. Access the app in your web browser at `http://localhost:8501`. 🌐

### Docker containerization

1. **Build Docker Image**:
   - Open your terminal and navigate to the project directory.
   - Run the following command to build the Docker image:
     ```
     docker build -t image-classification-app:latest .
     ```
   - This command will build a Docker image named `image-classification-app` with the latest tag.

2. **Run Docker Container**:
   - Once the Docker image is built successfully, you can run a Docker container using the following command:
     ```
     docker run -p 5000:5000 image-classification-app:latest
     ```
   - This command will start a Docker container based on the `image-classification-app` image and map port 5000 on your local machine to port 5000 in the container.

3. **Access the App**:
   - Open your web browser and navigate to `http://localhost:5000` to access the Image Classification App running inside the Docker container. 🚢

## Example

Suppose you upload an image of a dog. The app will predict that the image contains a "golden retriever" with a confidence score of 0.8 (80%). Additionally, it will suggest other possible labels and their confidence scores.