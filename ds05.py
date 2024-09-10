import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r"C:\Sheeba C\Prodigy Infotech\Tasks\accident-2014-4.csv")
# Check for missing values
print("Missing values in each column:")
print(df.isnull().sum())
print("\nFirst few rows of the dataset:")
print(df.head())
print("\nColumn names and data types:")
print(df.info())
print("\nBasic statistics:")
print(df.describe())

# Plot accident counts by road condition
plt.figure(figsize=(10, 6))
sns.countplot(x='Road Surface', data=df)
plt.title('Accidents by Road Condition')
plt.xlabel('Road Surface')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()
# Plot accident counts by weather condition
plt.figure(figsize=(10, 6))
sns.countplot(x='Weather Conditions', data=df)
plt.title('Accidents by Weather Condition')
plt.xlabel('Weather Conditions')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()
# Plot accident counts by time of day
plt.figure(figsize=(10, 6))
sns.countplot(x='Time (24hr)', data=df)
plt.title('Accidents by Time of Day')
plt.xlabel('Time (24hr)')
plt.ylabel('Number of Accidents')
plt.show()
