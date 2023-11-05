import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Step 2: Load and Prepare Data
data = pd.read_csv('data.csv')
X = data[['quiz1', 'quiz2', 'quiz3', 'pre', 'end']]
y = data['end']

# Step 3: Split Data
X_train, X_test, y_train, y_test = train_test_split(X[['quiz1', 'quiz2', 'quiz3', 'pre']], y, test_size=0.2, random_state=0)

# Step 4: Create and Train the Model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Make Predictions
y_pred = model.predict(X_test)

# Step 6: Evaluate the Model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"R-squared (R²): {r2}")

# Step 7: Visualize the Results (Optional)
import matplotlib.pyplot as plt
plt.scatter(X_test['quiz1'], y_test, color='blue')
plt.plot(X_test['quiz1'], y_pred, color='red', linewidth=2)
plt.xlabel('Quiz 1 Score')
plt.ylabel('End-Semester Result')
plt.title('Linear Regression: Quiz 1 vs. End-Semester Result')
plt.show()

# Step 8: Use the Model for Predictions
# You can use the 'model' to make predictions on new data if needed.
