# SALARY PREDICTION APP

Description
The Salary Prediction App is an interactive web application built using Streamlit and Python.<br>
This app predicts the salary of an employee based on their age and years of experience using a linear regression model. <br>
It provides a user-friendly interface to input data and visualize the results through scatter plots and heatmaps.<br>

Features
  -Data Loading and Caching: 
    Efficient data loading and caching using Streamlit's @st.cache_data to improve app performance.
  -Data Preprocessing and Model Training: 
    Preprocessing of data to handle features (Age and YearsExperience) and target variable (Salary).
    Splitting the dataset into training and testing sets.
    Training a Linear Regression model to predict salaries.
  -User Input for Predictions:
    User can input Age and Years of Experience.
    The app predicts and displays the salary based on the provided inputs.
  -Data Visualization:
    Scatter plot of Actual vs Predicted salaries.
    Heatmap showing correlations among features.

Installation Instruction
  1. Clone the Repository:
      git clone https://github.com/Gaurivn01/salaryprediction.git
      cd salaryprediction

  2. Create a Virtual Environment and Activate It:
      python -m venv env
      .\env\Scripts\activate

  3. Install the Required Packages:
      pip install -r requirements.txt

  4. Run the Streamlit App:
      streamlit run app.py

Usage Guidelines
  Launch the App:
    After running the above command, the app will start, and you will be provided with a local URL (e.g., http://localhost:8501). Open this URL in your web browser.

  Input Data:
    Enter the Age and Years of Experience in the respective input fields.

Predict Salary:
    Click on the "Predict Salary" button to get the predicted salary based on the input values.

Visualize Data:
    The app will display a scatter plot of actual vs. predicted salaries.
    A heatmap showing the correlations among different features in the dataset will also be displayed.


File Structure
    main.py: The main script for running the Streamlit app.
    requirements.txt: A list of dependencies required to run the app.
    Salary_Data.csv: The dataset used for training the model.
    
Enjoy using the Salary Prediction App! Your feedback and suggestions are welcome.
