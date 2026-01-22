import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import joblib

# Load data
data = pd.read_csv("house_data.csv")

X = data[['size_sqft', 'bedrooms', 'age']]
y = data['price']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Test model
predictions = model.predict(X_test)
print("Error:", mean_absolute_error(y_test, predictions))

# Save model
joblib.dump(model, "house_model.pkl")
