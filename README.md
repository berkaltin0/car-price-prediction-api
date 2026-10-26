# 🚗 Car Price Prediction API

## 📌 Overview
This repository contains a robust Machine Learning pipeline and a REST API for predicting the selling price of used cars. The predictive model was trained using **AutoGluon**, and the deployment is handled via **FastAPI** and **Docker**, making it fully production-ready.

## 🚀 Features
- **Advanced AutoML:** Utilizes AutoGluon for high-performance tabular prediction (featuring advanced models like ExtraTrees, RandomForest, etc.).
- **FastAPI Integration:** Fast, asynchronous, and self-documenting REST API for real-time inference.
- **Dockerized:** Containerized application for seamless deployment across any environment without dependency conflicts.
- **Git LFS:** Efficiently handles large pre-trained model files (`.pkl`).

## 📂 Project Structure
- `app.py`: Main FastAPI application script handling routing and prediction logic.
- `Dockerfile`: Instructions for building the Docker image.
- `requirements.txt`: Python dependencies required to run the project.
- `autogluon_car_model/`: Directory containing the exported AutoGluon models.
- `drift_car_analysis.ipynb`: Jupyter Notebook detailing Exploratory Data Analysis (EDA), missing value imputation, feature engineering, and baseline model training.

## ⚙️ How to Run Locally

### Prerequisites
Ensure you have [Git LFS](https://git-lfs.github.com/) installed before cloning the repository to properly download the large model files.

```bash
# 1. Clone the repository
git clone [https://github.com/berkaltin0/car-price-prediction-api.git](https://github.com/berkaltin0/car-price-prediction-api.git)
cd car-price-prediction-api

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the FastAPI server
uvicorn app:app --reload
