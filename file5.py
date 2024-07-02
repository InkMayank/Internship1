
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.read_csv('D:\heart.csv')  

# Explore the data
print("Dataset Head:")
print(df.head())
print("\nDataset Info:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())

# Creating a new feature by combining existing ones
df['new_feature'] = df['age'] * df['sex']  # Replace with relevant features

# Separating features and target variable
X = df.drop(columns=['target'])  # Replace 'target' with your actual target variable name
y = df['target']  # Replace 'target' with your actual target variable name

# Standardizing the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# PCA for dimensionality reduction (if needed)
pca = PCA(n_components=0.95)  # Retain 95% of variance
X_pca = pca.fit_transform(X_scaled)
print("\nExplained variance by PCA components:")
print(pca.explained_variance_ratio_)

# Feature importance using Random Forest
model = RandomForestClassifier()
model.fit(X, y)
importances = model.feature_importances_
feature_importance = pd.DataFrame({'feature': X.columns, 'importance': importances})
feature_importance = feature_importance.sort_values(by='importance', ascending=False)
print("\nFeature Importance:")
print(feature_importance)

# Selecting top important features
top_features = feature_importance.head(10)['feature'].tolist()  # Selecting top 10 features
X_top_features = df[top_features]

# Optimize feature sets for improved model performance
X_train, X_test, y_train, y_test = train_test_split(X_top_features, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("\nModel Accuracy with Selected Features:", accuracy)

# Save the final dataset with selected features
df_top_features = df[top_features + ['target']]  # Include target column
df_top_features.to_csv('path_to_save_selected_features.csv', index=False)  # Save to CSV

print("\nSelected Features Dataset Saved!")
