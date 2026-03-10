import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

data = pd.read_csv("house_data.csv")

# Seprating input and target feature
X = data[['Size', 'Bedrooms', 'Age']]
y = data['Price']

# creating linear regression model
model = LinearRegression()
model.fit(X, y)

joblib.dump(model,"house_model.pkl")
print("Model trained successfully and saved as house_model.pkl")