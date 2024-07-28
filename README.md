# SALARY PREDICTION APP

Description
The Salary Prediction App is an interactive web application built using Streamlit and Python.<br>
This app predicts the salary of an employee based on their age and years of experience using a linear regression model. <br>
It provides a user-friendly interface to input data and visualize the results through scatter plots and heatmaps.<br>
<br>
Features
  -Data Loading and Caching: <br>
    Efficient data loading and caching using Streamlit's @st.cache_data to improve app performance.<br>
  -Data Preprocessing and Model Training: <br>
    Preprocessing of data to handle features (Age and YearsExperience) and target variable (Salary).<br>
    Splitting the dataset into training and testing sets.<br>
    Training a Linear Regression model to predict salaries.<br>
  -User Input for Predictions:<br>
    User can input Age and Years of Experience.<br>
    The app predicts and displays the salary based on the provided inputs.<br>
  -Data Visualization:<br>
    Scatter plot of Actual vs Predicted salaries.<br>
    Heatmap showing correlations among features.<br>
<br>
Installation Instruction
  1. Clone the Repository:<br>
      git clone https://github.com/Gaurivn01/salaryprediction.git<br>
      cd salaryprediction<br><br>

  2. Create a Virtual Environment and Activate It:<br>
      python -m venv env<br>
      .\env\Scripts\activate<br>

  3. Install the Required Packages:<br>
      pip install -r requirements.txt<br>

  4. Run the Streamlit App:<br>
      streamlit run app.py<br><br>

Usage Guidelines<br>
  Launch the App:<br>
    After running the above command, the app will start, and you will be provided with a local URL (e.g., http://localhost:8501). Open this URL in your web browser.

  Input Data:<br>
    Enter the Age and Years of Experience in the respective input fields.<br>

Predict Salary:<br>
    Click on the "Predict Salary" button to get the predicted salary based on the input values.<br>

Visualize Data:<br>
    The app will display a scatter plot of actual vs. predicted salaries.<br>
    A heatmap showing the correlations among different features in the dataset will also be displayed.<br>


File Structure<br>
    main.py: The main script for running the Streamlit app.<br>
    requirements.txt: A list of dependencies required to run the app.<br>
    Salary_Data.csv: The dataset used for training the model.<br>
    
Enjoy using the Salary Prediction App! Your feedback and suggestions are welcome.
