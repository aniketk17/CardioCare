# CardioCare

## Overview
CardioCare is a project designed to predict heart disease using machine learning. It incorporates a predictive model that analyzes various health metrics and provides insights into the likelihood of heart disease. This project also includes a Jupyter Notebook for exploratory data analysis and model training.

## Features
- **Heart Disease Prediction**: Uses machine learning algorithms to predict the risk of heart disease.
- **Jupyter Notebook**: Contains code for data preprocessing, model training, and evaluation.
- **User Management**: Allows users to register and log in to access personalized features.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: [Django]
- **Database**: [MySQL]
- **Machine Learning**: Python, scikit-learn, pandas, NumPy

## Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/aniketk17/Pbl-2.git


2. Create Virtual Environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
 
3. Install Dependencies:
   ```bash
   pip install -r requirements.txt

4. Apply Database migrations:
   ```bash
   python manage.py migrate
   python manage.py makemigrations

5. Create a superuser to access the admin dashboard:
   ```bash
   python manage.py createsuperuser

6. Start the development server:
   ```bash
   python manage.py runserver
