# Project-4-Cost of Living


Group 2: Project 4 - Cost of Living Analysis

**Group Members:**
- Brittany Castro
- Cooper Harris
- Lois Stetson
- Thanh Vo

**Data Project Proposal: Cost of Living in the US**

**Introduction:**
The objective is to analyze the cost of living using a machine learning model. The project aims to develop and optimize a predictive model that estimates the cost of living based on various features. This assists in compensation planning for future employees, considering location factors.

**Data Source:**
[US Cost of Living Dataset](https://www.kaggle.com/datasets/asaniczka/us-cost-of-living-dataset-3171-counties?rvi=1)

**Problem Statement: Analyzing Cost of Living with Machine Learning**
The project focuses on leveraging machine learning for a comprehensive cost of living analysis. It involves data cleaning, normalization, and standardization processes. Utilizing data from Spark enhances data processing capabilities, aiming for meaningful predictive power. The goal is to optimize the model, document changes, and showcase overall performance, providing insights into cost of living dynamics.

**Project Overview:**

**Data Model Implementation:**
1. **Initialization, Training, and Evaluation:**
   - Develop a Python script using popular ML libraries like sklearn.
2. **Data Cleaning, Normalization, and Standardization:**
   - Implement processes to handle missing values and outliers.
   - Normalize and standardize features for consistent scaling.
3. **Utilization of Data from Spark:**
   - Incorporate data retrieval from Spark to enhance processing capabilities.
4. **Meaningful Predictive Power:**
   - Ensure the model achieves at least 75% classification accuracy or 0.80 R-squared.

**Data Model Optimization:**
1. **Optimization and Evaluation Documentation:**
   - Document the iterative model optimization process.
   - Record changes and impacts in a CSV/Excel table or within the Python script.
2. **Overall Model Performance Display:**
   - Print or display overall model performance.
   - Provide insights into effectiveness and areas for improvement.

**Proposed Timeline:**
- **Week 1:** Project Initialization
  - Review existing Jupyter notebook and understand the dataset.
  - Set up project structure and initialize version control.
- **Week 2:** Data Preparation and Cleaning
  - Implement data cleaning processes and handle outliers.
  - Normalize and standardize features.
- **Week 3:** Model Implementation
  - Develop Python script for initializing, training, and evaluating the model.
  - Incorporate data retrieval from Spark.
- **Week 4:** Model Optimization
  - Document model optimization process and changes.
  - Display overall model performance.
- **Week 5:** Finalization and Documentation
  - Perform final testing and validation.
  - Document the entire process with code comments and explanations.

**Expected Deliverables:**
1. Python script (`Cost_of_Living.py`) with the implemented model and data processing steps.
2. Documentation highlighting the model optimization process, including a CSV/Excel table or in-code comments.
3. Comprehensive README file explaining project structure, dependencies, and instructions for running the script.

**Team Members and Responsibilities:**
1. **Data Cleaning and Processing:**
   - Responsibilities: Implement data cleaning processes and feature engineering.
2. **Model Implementation:**
   - Responsibilities: Develop Python script for initializing, training, and evaluating the model.
3. **Data Retrieval and Integration:**
   - Responsibilities: Retrieve data from Spark and integrate it into the script.
4. **Model Optimization and Documentation:**
   - Responsibilities: Document the model optimization process and overall model performance.
   
**Conclusion:**
This project aims to create a robust machine learning model for cost of living analysis. The proposed timeline and responsibilities ensure a systematic approach to achieve the project objectives.


Our initial cleaning, we started by dropping unnecessary columns, looking for missing values and dropping those rows with missing values, and also separating out the family member count column to create three new columns one to represent parents in the home, children in the home, and an overall family size amount column. Then we moved into exploring the dataset.


**Histogram**
Insights:
•	Peaks and patterns in histograms can indicate central tendencies and variations in the data.
•	Skewness or symmetry in distributions may be observed.
•	Outliers or unusual patterns might be identified.
Key Takeaways:
•	Histograms are valuable for initial data exploration and understanding the spread of variables.
•	They help identify data patterns, potential outliers, and insights into the data's central tendencies.
Utilizing histograms is an essential step in the exploratory data analysis process, offering a visual overview of the dataset's distribution characteristics.

![Histograms_for_distribution](https://github.com/loisstetson/Project-4-Cost-of-Living/assets/127718619/9afae3bf-5574-4a36-9044-18881721353a)

 
 
**Correlation Matrix**
Using sns in python, we created a correlation matrix
In the correlation matrix, The colors indicate the strength and direction of correlations, with warmer colors (reds) representing positive correlations and cooler colors (blues) representing negative correlations. The numerical annotations provide precise correlation values for each pair of variables. This visualization is crucial for identifying patterns and dependencies in the data.

![correlation_matrix](https://github.com/loisstetson/Project-4-Cost-of-Living/assets/127718619/f6990ce0-1be4-4ca4-8d3b-7803855cc265)


**Correlation Plot**
Presentation Explanation:
•	Objective: The objective of this visualization is to explore the relationships and distributions between selected features in the dataset.
•	Pair Plot: The pair plot provides a quick overview of the pairwise relationships between features. Each scatterplot shows how two variables interact with each other.
•	Diagonal Plots (KDE): The diagonal plots represent the distribution of individual features using KDE. This helps in understanding the shape and spread of each variable's values.
•	Off-Diagonal Plots: These scatterplots show the relationships between pairs of features. Patterns, trends, or clusters in these plots can indicate potential correlations or associations.
Insights:
•	Correlation Assessment: Look for patterns in the off-diagonal scatterplots to identify potential correlations between variables.
•	Distribution Understanding: Diagonal KDE plots provide insights into the distribution of each feature, helping to understand the data's characteristics.
Key Points:
•	Title Clarity: The title 'Correlations' suggests a focus on relationships between variables.
•	Visualizing Data Patterns: Pair plots are effective for visualizing multivariate patterns and can aid in feature selection and understanding data distributions.

![correlation_plots](https://github.com/loisstetson/Project-4-Cost-of-Living/assets/127718619/a348892d-f5e3-4713-8089-2d2963b942b6)


**Machine Learning Model**

![image](https://github.com/loisstetson/Project-4-Cost-of-Living/assets/127718619/27f42ff1-6a91-4e80-8fa4-da9820e08b42)


![image](https://github.com/loisstetson/Project-4-Cost-of-Living/assets/127718619/07bc230d-3188-4ce0-864b-292a6b571ea7)

![image](https://github.com/loisstetson/Project-4-Cost-of-Living/assets/127718619/68186ed3-153f-411c-95cb-e3a2091e5277)

**Analysis & Visualizations**

![Average_income by state](https://github.com/loisstetson/Project-4-Cost-of-Living/assets/127718619/6dfcd5ca-06a6-4dba-a82b-d0a9db87d3a0)
This shows a horizontal bar plot is created to visualize the average annual family income across different US states. The resulting visualization is a horizontal bar plot that effectively communicates the average annual family income for each US state. The annotations provide specific values, and the color palette enhances the overall aesthetics of the plot. Overall, DC has the highest Average Annual Income and Mississippi has the lowest Average Annual Income.
![area plots](https://github.com/loisstetson/Project-4-Cost-of-Living/assets/127718619/037a3914-65cb-4ac8-8b22-4d20ddbe1e87)

![boxplots for every iteration](https://github.com/loisstetson/Project-4-Cost-of-Living/assets/127718619/27a68395-f913-4cf9-837a-00ff1c36295e)

![housing_cost_choropleth](https://github.com/loisstetson/Project-4-Cost-of-Living/assets/127718619/4b5a02b0-b06b-4050-84e8-c74e41e62122)




