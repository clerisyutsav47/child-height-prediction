# Child Height Prediction
This is a streamlit web application for height prediction using a neural network model. The application uses a combination of raw and wavelet transformed image features to make predictions. The model was trained using Tensorflow/Keras.

# Installation

Clone the repository and navigate to the root folder:
```terminal
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

Create a virtual environment: 
```terminal
python3 -m venv venv
```

Activate the virtual environment:  
On Windows:  
```terminal
venv\Scripts\activate
```

On Linux or macOS:
```terminal
source venv/bin/activate
```

Install the dependencies: 
```terminal
pip install -r requirements.txt
```

# Usage
To run the application, navigate to the root folder and execute the following command:  
```terminal
python app.py
```
Then, open a web browser and go to http://localhost:5000/.
Upload an image and the application will predict the height of the image using the pre-trained machine learning model.

# Files
* app.py: This is the streamlit web application that serves as the main entry point of the program. It uses the machine learning model to predict the face in an uploaded image.

* main.py: This is the Python script that trains the machine learning model using Scikit-learn, OpenCV, and PyWavelets libraries.

* model.pkl: This is the pre-trained machine learning model.



# License
This project is protected by the MIT License. See the LICENSE file for more details.

# Credits
* This project was created by Utsav Acharya.
* The Tensorflow library was used for the model.
* The streamlit web framework was used to create the web application.

 



