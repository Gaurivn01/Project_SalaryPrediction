import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
@st.cache_data  # Cache the dataset to improve app performance
def load_data():
    data = pd.read_csv("C:\\Users\\gauri\\OneDrive\\Desktop\\Salary_Data.csv")
    return data

# Preprocess the data and train the model
def preprocess_and_train(data):
    # Assuming 'Age' and 'YearsExperience' are the features, and 'Salary' is the target variable
    X = data[['Age', 'YearsExperience']]
    y = data['Salary']
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    return model, X_test, y_test

# Predict salary based on user input
def predict_salary(model, age, years_exp):
    salary = model.predict([[age, years_exp]])
    return salary[0]

# Create scatter plot of actual vs predicted salaries
def plot_actual_vs_predicted(model, X_test, y_test):
    y_pred = model.predict(X_test)
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.scatter(y_test, y_pred)
    ax.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], 'k--', lw=2)
    ax.set_xlabel("Actual Salary")
    ax.set_ylabel("Predicted Salary")
    ax.set_title("Actual vs Predicted Salary")
    st.pyplot(fig)

# Create heatmap to show correlations
def plot_heatmap(data):
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

# Create the Streamlit app
def main():
    st.title("Salary Prediction App")

    # Load the dataset
    data = load_data()

    # Preprocess the data and train the model
    model, X_test, y_test = preprocess_and_train(data)

    # User inputs
    age = st.number_input("Enter Age:")
    years_exp = st.number_input("Enter Years of Experience:")

    # Predict button
    if st.button("Predict Salary"):
        salary_prediction = predict_salary(model, age, years_exp)
        st.success(f"Predicted Salary: ${salary_prediction:.2f}")

    # Plot actual vs predicted salaries
    plot_actual_vs_predicted(model, X_test, y_test)

    # Plot heatmap
    plot_heatmap(data)

if __name__ == "__main__":
    main()
