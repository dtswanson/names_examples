import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Generate synthetic data
np.random.seed(42)
data_size = 100

# Data and their relationships
months = np.random.choice(['November', 'December', 'January', 'February'], data_size)
temperature = np.random.normal(0, 10, data_size)  # Average temperature in winter
snowfall = np.random.normal(50, 20, data_size)  # Snowfall in cm
holiday_bookings = np.random.normal(200, 50, data_size)  # Number of holiday bookings

# Encode months as numbers
month_mapping = {'November': 1, 'December': 2, 'January': 3, 'February': 4}
months_encoded = np.array([month_mapping[month] for month in months])

# Target variable: Ski season quality
ski_season_quality = 0.1 * months_encoded + 0.3 * temperature + 0.5 * snowfall + 0.2 * holiday_bookings + np.random.normal(0, 5, data_size)

# Create DataFrame
data = pd.DataFrame({
    'Month': months,
    'Temperature': temperature,
    'Snowfall': snowfall,
    'Holiday_Bookings': holiday_bookings,
    'Ski_Season_Quality': ski_season_quality
})

# Summary of the data
summary = data.describe(include='all')
print("Summary of the data:")
print(summary)

# Visualization
plt.figure(figsize=(12, 8))

# Pairplot
sns.pairplot(data, hue='Month')
plt.suptitle('Pairplot of Southern Bavaria Ski Season Data 2024/2025 Season', y=1.02)

# Encode months as numerical values for correlation calculation
data['Month_Encoded'] = data['Month'].map(month_mapping)

# Drop the original 'Month' column for correlation calculation
data_for_corr = data.drop(columns=['Month'])

# Correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(data_for_corr.corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Southern Bavaria Ski Season Data 2024/2025 Season Correlation Heatmap')

# Show plots
plt.show()

# Split the data into training and testing sets
X = pd.get_dummies(data[['Month', 'Temperature', 'Snowfall', 'Holiday_Bookings']], drop_first=True)
y = data['Ski_Season_Quality']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# making the regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')