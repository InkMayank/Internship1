import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

data = pd.read_csv("D:\disney_plus_titles.csv")

# Convert date_added to datetime
data['date_added'] = pd.to_datetime(data['date_added'])

# Time Series Analysis
# Count shows added per month
data['month_added'] = data['date_added'].dt.to_period('M')
monthly_additions = data.groupby('month_added').size()

# Plot the time series
plt.figure(figsize=(12, 6))
monthly_additions.plot()
plt.title('Number of Shows Added Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Shows Added')
plt.show()

# Sentiment Analysis using VADER
analyzer = SentimentIntensityAnalyzer()
data['description_sentiment'] = data['description'].apply(lambda x: analyzer.polarity_scores(x)['compound'])

# Plot sentiment polarity
plt.figure(figsize=(12, 6))
sns.histplot(data['description_sentiment'], bins=20, kde=True)
plt.title('Sentiment Polarity of Descriptions')
plt.xlabel('Sentiment Polarity')
plt.ylabel('Frequency')
plt.show()

# Clustering/Classification
# Vectorize the 'listed_in' column
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(data['listed_in'])

# Apply KMeans clustering
kmeans = KMeans(n_clusters=5, random_state=42)
data['cluster'] = kmeans.fit_predict(X)

# Reduce dimensions for visualization
pca = PCA(n_components=2)
components = pca.fit_transform(X.toarray())

# Plot clusters
plt.figure(figsize=(12, 6))
plt.scatter(components[:, 0], components[:, 1], c=data['cluster'], cmap='viridis')
plt.title('KMeans Clustering of Shows by Genre')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.show()

# Display the first few rows of the modified data
print(data[['title', 'month_added', 'description_sentiment', 'cluster']].head())
