import pandas as pd

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv(r'D:\student-dataset (1).csv')
print("Data loaded into DataFrame:")
print(df.head())

# Filter data based on conditions
filtered_df = df[df['age'] > 21]  # Replace 'age' with an appropriate column name
print("Filtered DataFrame (age > 21):")
print(filtered_df.head())

# Handle missing values
# Drop missing values
df_dropped = df.dropna()
print("DataFrame after dropping rows with missing values:")
print(df_dropped.head())

# Fill missing values with column mean
# Select only numeric columns
numeric_cols = df.select_dtypes(include='number').columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
print("DataFrame after filling missing values in numeric columns with column mean:")
print(df.head())

# Calculate summary statistics
summary_stats = df.describe()
print("Summary statistics:")
print(summary_stats)

# Additional statistics
total_sum = df['age'].sum()  # Replace 'age' with an appropriate column name
mean_value = df['age'].mean()
median_value = df['age'].median()
print(f"Sum of ages: {total_sum}")
print(f"Mean age: {mean_value}")
print(f"Median age: {median_value}")
