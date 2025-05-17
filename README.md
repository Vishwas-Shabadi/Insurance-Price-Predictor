📊 Health Insurance Premium Prediction

📝 Problem Statement

The goal of this project is to build a predictive model that estimates health insurance premium prices based on an individual’s health profile, medical history, and demographic attributes.

Insurance companies often struggle with accurately pricing premiums, especially when health data is diverse and includes both numeric and categorical factors. An accurate, data-driven model would allow insurers to offer fair pricing, manage risks, and improve customer satisfaction.

🎯 Target Metric

* Primary Metric: R² (Coefficient of Determination)
* To measure the proportion of variance in premium prices explained by the independent variables.

Secondary Metrics:

* RMSE (Root Mean Squared Error)
* MAE (Mean Absolute Error)

🛠️ Project Workflow

📌 1. Exploratory Data Analysis (EDA)

* Examined data distributions, outliers, and missing values.
* Visualized relationships between health metrics and premium prices.
* Key observations:

  * Premium prices increase with age, BMI, and number of surgeries.
  * Certain conditions like diabetes and chronic diseases affect premiums significantly.

📌 2. Hypothesis Testing

* Conducted statistical tests to validate assumptions:

  * **T-tests** and **ANOVA** for mean premium differences across categorical variables.
  * Confirmed that factors like **chronic diseases** and **multiple surgeries** have statistically significant effects on premiums.

📌 3. Feature Engineering

Derived additional features to capture complex relationships:

* BMI (Body Mass Index)
* MultipleSurgeries flag (if > 2 surgeries)
* OtherHealthConditions count
* Categorical groupings based on age and BMI ranges.

📌 4. Machine Learning Modelling

Models Used:

* Linear Regression (Baseline)
* Decision Tree Regressor
* Random Forest Regressor
* Gradient Boosting Regressor

Model Selection:

* Evaluated models using R², RMSE, and MAE.
* Performed hyperparameter tuning using GridSearchCV for ensemble models.

Final Model:

* Gradient Boosting Regressor
* R² Score:** 0.85
* RMSE: 231.38
* MAE: 161.21

Best trade-off between accuracy and overfitting prevention.

🚀 Deployment

* Created a Flask REST API endpoint to serve the model.
* Developed a Streamlit web app for interactive predictions.
* Packaged model and scaler objects via Pickle.
* Tested both local and cloud-based deployments using Postman and web interfaces.

📊 Insights & Recommendations

📌 Data Insights

1. Premium prices increase significantly after age 50.
2. Higher BMI categories (Obese, Overweight) correlate with higher premiums.
3. Multiple major surgeries drastically increase premium costs.
4. Individuals with chronic diseases pay notably higher premiums.
5. Total number of health conditions strongly impacts premium predictions.
6. Diabetes and blood pressure issues individually lower premiums, but total health issues increase them.
7. Young adults (Age < 30) generally receive lower premiums.
8. Premium per surgery is a major cost contributor.
9. RiskIndex is a crucial variable for premium adjustment.
10. Certain BMI groups, like underweight individuals, don’t show strong premium impacts.

📌 Business Recommendations

1. Incorporate health issue counts and surgery counts into underwriting systems.
2. Use predictive models for early premium estimation during onboarding.
3. Offer targeted health management programs for high BMI or high-risk individuals.
4. Provide wellness incentives for younger policyholders.
5. Leverage risk-based pricing dynamically instead of fixed premium slabs.
6. Monitor total health conditions for proactive policy updates.
7. Apply loadings for individuals with multiple surgeries.
8. Optimize premium structures by age and BMI groups.
9. Use ensemble models (like Gradient Boosting) for production deployments.
10. Regularly review model performance and recalibrate with new data.

📦 Tech Stack

* Python
* Pandas, NumPy, Matplotlib, Seaborn
* Scikit-learn
* Statsmodels
* Streamlit
* Flask
* Pickle
* Google Colab

📂 Project Structure

📦 Insurance-Premium-Prediction/
 ┣ 📂 model/
 ┃ ┣ model.pkl
 ┃ ┣ scaler.pkl
 ┣ 📂 app/
 ┃ ┣ app.py
 ┃ ┣ streamlit_app.py
 ┣ 📄 EDA_Notebook.ipynb
 ┣ 📄 requirements.txt
 ┣ 📄 README.md


📌 Conclusion

This project successfully demonstrates a comprehensive end-to-end machine learning pipeline — from EDA to deployment — for predicting health insurance premiums. The final model shows strong predictive performance, and the accompanying insights can meaningfully improve insurance pricing strategies.

