# src/model.py

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib
from data_processing import load_data, preprocess_data
import pandas as pd

# Load & preprocess
df = preprocess_data(load_data())

X = df[['experience_level','employment_type','job_title','remote_ratio','company_location']]
y = df['salary']

categorical_features = ['experience_level','employment_type','job_title','company_location']
numeric_features = ['remote_ratio']

preprocessor = ColumnTransformer([
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features),
    ('num', 'passthrough', numeric_features)
])

model = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=200, random_state=42))
])

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("MAE:", mean_absolute_error(y_test, y_pred))
print("RMSE:", mean_squared_error(y_test, y_pred, squared=False))

# Save model in src/ folder
joblib.dump(model, "tech_salary_model.pkl")
print("Model saved as src/tech_salary_model.pkl")

# Optional: sample prediction
sample = pd.DataFrame({
    'experience_level':['SE'],
    'employment_type':['FT'],
    'job_title':['Data Scientist'],
    'remote_ratio':[50],
    'company_location':['US']
})
pred_salary = model.predict(sample)
print("Predicted Salary:", pred_salary[0])