# Tech Job Salary Prediction & Dashboard

This project predicts tech job salaries based on experience, role, location, remote work, and employment type. It also includes a **Power BI dashboard** visualizing key metrics and trends in the tech job market.

---

## Project Overview

- **Goal:** Analyze global tech job salaries and build a prediction model.  
- **Dataset:** `salaries.csv` containing AI/ML/Data Science and tech roles across multiple countries, with fields like:  
  - `work_year`, `experience_level`, `employment_type`, `job_title`  
  - `salary`, `salary_currency`, `remote_ratio`, `company_location`, `employee_residence`  
- **Tech Used:** Python (pandas, scikit-learn), Power BI, Random Forest Regressor.

---

## Folder Structure


TechJobSalaryPrediction/
│
├── data/ # Dataset
│ └── salaries.csv
├── notebooks/ # EDA and modeling
│ └── EDA_and_Model.ipynb
├── src/ # Python scripts
│ ├── data_processing.py
│ └── model.py
├── visuals/ # Charts and dashboard
│ ├── TechJobSalaryDashboard.pdf
│ ├── dashboard_overview.png
│ ├── top_jobs.png
│ └── salary_experience.png
├── TechJobSalaryDashboard.pbix
├── README.md
└── requirements.txt


---

## Key Features

- Predict tech job salaries using `RandomForestRegressor`.  
- Visualize salary trends:  
  - **Top 10 Job Titles by Average Salary**  
  - **Salary by Experience Level**  
  - **Salary by Location**  
  - **Remote Ratio vs Salary**  
  - **Employment Type Distribution**  
- Interactive dashboard with slicers for filtering by job title, location, experience, and employment type.  

---

## Dashboard Preview

**Power BI dashboard PDF:**  
[Download Dashboard PDF](visuals/TechJobSalaryDashboard.pdf)

**Screenshots (inline preview):**

![Dashboard Overview](visuals/dashboard_overview.png)  
![Top 10 Jobs](visuals/top_jobs.png)  
![Salary by Experience](visuals/salary_experience.png)

---

## How to Run the Notebook

1. Clone the repository:  
```bash
git clone https://github.com/YOUR_USERNAME/TechJobSalaryPrediction.git

Install dependencies:

pip install -r requirements.txt

Open the notebook in Jupyter or VSCode and run:

notebooks/EDA_and_Model.ipynb

The trained model will be saved as:

src/tech_salary_model.pkl

Example to test predictions:

import pandas as pd
import joblib

model = joblib.load('src/tech_salary_model.pkl')
sample = pd.DataFrame({
    'experience_level':['SE'],
    'employment_type':['FT'],
    'job_title':['Data Scientist'],
    'remote_ratio':[50],
    'company_location':['US']
})
pred_salary = model.predict(sample)
print("Predicted Salary:", pred_salary[0])
Dataset Source

Original dataset: Kaggle – Data Jobs Salaries
