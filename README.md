

# Crop Prediction Application

This Flask-based web application predicts the best crop to be cultivated based on several input parameters such as Nitrogen, Phosphorus, Potassium levels, temperature, humidity, pH, and rainfall.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Model and Scalers](#model-and-scalers)
- [Routes](#routes)
- [File Structure](#file-structure)
- [Acknowledgements](#acknowledgements)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/crop-prediction-app.git
   cd crop-prediction-app
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure that the following files are in the project directory**:
   - `model.pkl`: The trained machine learning model.
   - `standscaler.pkl`: The StandardScaler object used during model training.
   - `minmaxscaler.pkl`: The MinMaxScaler object used during model training.

## Usage

1. **Run the application**:
   ```bash
   python app.py
   ```
   The application will start running on `http://127.0.0.1:5000/`.

2. **Access the application**:
   Open a web browser and go to `http://127.0.0.1:5000/`.

3. **Input the required data**:
   - Nitrogen (N)
   - Phosphorus (P)
   - Potassium (K)
   - Temperature
   - Humidity
   - pH
   - Rainfall

4. **Get the prediction**:
   After submitting the form, the application will display the best crop to be cultivated based on the input data.

## Model and Scalers

- **Model**: The application uses a machine learning model (likely a classifier) stored in `model.pkl` to predict the best crop.
- **Scalers**:
  - `standscaler.pkl`: A `StandardScaler` object to standardize features by removing the mean and scaling to unit variance.
  - `minmaxscaler.pkl`: A `MinMaxScaler` object to scale features to a given range (default: [0, 1]).

These scalers are used to transform the input data before making predictions with the model.

## Routes

- **`/` (GET)**: Renders the main page (`index.html`) where users can input data.
- **`/predict` (POST)**: Accepts input data from the form, processes it, and returns the crop prediction.

## File Structure

```
├── app.py                 # The main Flask application
├── model.pkl              # The trained machine learning model
├── standscaler.pkl        # StandardScaler object
├── minmaxscaler.pkl       # MinMaxScaler object
├── templates
│   └── index.html         # HTML template for the main page
├── static
│   └── (optional static files like CSS, JS)
└── README.md              # This README file
```

## Acknowledgements

This application is built using Flask and leverages scikit-learn for machine learning tasks. The model and scalers should be trained separately and loaded into the application.

## Screenshots
![Screenshot 2024-08-16 015347](https://github.com/user-attachments/assets/7c16c98b-aaba-4d8c-94e1-f83acd8898cf)
![Screenshot 2024-08-16 015307](https://github.com/user-attachments/assets/4fe6ec2c-7991-40f8-a413-ab120653f628)

