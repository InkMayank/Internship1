import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
data = {
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Values': [10, 20, 15, 25, 30],
    'Trends': [12, 18, 14, 28, 35]
}

df = pd.DataFrame(data)


# Create Bar Chart
plt.figure(figsize=(10, 6))
plt.bar(df['Category'], df['Values'], color='skyblue', label='Values')
plt.xlabel('Category')
plt.ylabel('Values')
plt.title('Bar Chart Example')
plt.legend()
plt.show()  # Ensure this is called to display the plot

# Create Line Chart
plt.figure(figsize=(10, 6))
plt.plot(df['Category'], df['Trends'], marker='o', color='orange', label='Trends')
plt.xlabel('Category')
plt.ylabel('Trends')
plt.title('Line Chart Example')
plt.legend()
plt.show()  # Ensure this is called to display the plot

