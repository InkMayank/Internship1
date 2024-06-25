import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Data
df = pd.read_csv('D:\StudentsPerformance.csv')

# Step 2: Initial Inspection
print(df.head())
print(df.info())
print(df.describe())

# Data Cleaning
# Missing Values
print(df.isnull().sum())

# Separate numeric and non-numeric columns
numeric_cols = df.select_dtypes(include=np.number).columns
non_numeric_cols = df.select_dtypes(exclude=np.number).columns

# Fill missing values in numeric columns with the mean
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# Fill missing values in non-numeric columns with the mode
df[non_numeric_cols] = df[non_numeric_cols].apply(lambda col: col.fillna(col.mode()[0]))

# Duplicates
print(df.duplicated().sum())
df.drop_duplicates(inplace=True)

# Univariate Analysis
# Ensure to replace 'your_categorical_column' with an actual column name
categorical_column = 'gender'  # Replace with actual column name
if categorical_column in df.columns:
    df[categorical_column].value_counts().plot(kind='bar')
    plt.show()

# Numerical Variables
numerical_column = 'math score'  # Replace with actual column name
if numerical_column in df.columns:
    df[numerical_column].plot(kind='hist', bins=30)
    plt.show()

# Bivariate Analysis
# Ensure to replace these with actual column names
numerical_column1 = 'reading score'  # Replace with actual column name
numerical_column2 = 'writing score'  # Replace with actual column name
if numerical_column1 in df.columns and numerical_column2 in df.columns:
    sns.scatterplot(x=numerical_column1, y=numerical_column2, data=df)
    plt.show()

# Correlation Heatmap
# Use only numeric columns for correlation matrix
corr = df[numeric_cols].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()

# Outlier Detection
# Ensure to replace 'your_numerical_column' with an actual column name
if numerical_column in df.columns:
    sns.boxplot(x=numerical_column, data=df)
    plt.show()


