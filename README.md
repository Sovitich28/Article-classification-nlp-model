# News Article Category Predictor

A machine learning application that automatically categorizes news articles using Natural Language Processing (NLP) and Multinomial Naive Bayes classification.

## Academic Context

This project was developed as part of the Natural Language Processing (NLP) course at the Higher School of Computer Science - ESI Sidi Bel Abbes (École Supérieure en Informatique de Sidi Bel Abbès). It demonstrates the practical application of NLP concepts and machine learning techniques in text classification.

## Overview

This project implements a news article classification system that can automatically categorize news articles into different categories. The system uses a Multinomial Naive Bayes classifier trained on the BBC News dataset and achieves high accuracy in predicting article categories.

## Features

- Text-based news article classification
- Interactive web interface using Streamlit
- High accuracy classification (96% test accuracy)
- Real-time prediction capabilities
- User-friendly interface for article input

## Project Structure

```
├── app.py                         # Streamlit web application
├── BBC News Test.csv             # Test dataset
├── BBC News Train.csv            # Training dataset
├── NB_model.pkl                  # Trained Naive Bayes model
├── News_Article_Classifier.ipynb  # Model training notebook
└── README.md                     # Project documentation
```

## Technologies Used

- Python
- Streamlit
- scikit-learn
- NumPy
- Jupyter Notebook

## Getting Started

1. Install the required dependencies:
```bash
pip install streamlit numpy scikit-learn joblib
```

2. Run the Streamlit application:
```bash
streamlit run app.py
```

3. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

## Usage

1. Access the web interface through your browser
2. Enter the news article text in the provided text area
3. Click the "Predict Category" button
4. View the predicted category for your article

## Model Performance

The Multinomial Naive Bayes model achieves:
- Training Accuracy: 99%
- Test Accuracy: 96%
- High precision and recall across different news categories

## License

This project is available for educational and research purposes.