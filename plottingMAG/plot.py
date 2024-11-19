import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
print("Setup Complete")

magnesium_filepath = "/Users/dswanson/PycharmProjects/Names/plottingMAG/ExperimentMagnesiumActual.csv"
magnesium_data = pd.read_csv(magnesium_filepath, delimiter=';')
magnesium_data.columns = magnesium_data.columns.str.strip()

# Print columns to verify
print(magnesium_data.columns)

# Correct plotting
sns.lineplot(x='Time', y='Temperature', data=magnesium_data)  # Ensure these column names match your CSV file
plt.show()