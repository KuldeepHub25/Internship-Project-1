# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 20:53:03 2025

@author: Kuldeep
"""

import pandas as pd 
a=pd.read_csv("C:\\Users\\Kuldeep Mishra\\Downloads\\AB_NYC_2019.csv")
print(a)
import pandas as pd

# Load the dataset (already done by you)
a = pd.read_csv("C:\\Users\\Kuldeep Mishra\\Downloads\\AB_NYC_2019.csv")

# Step 1: Clean the data by removing rows with missing critical values
a_cleaned = a.dropna(subset=['price', 'room_type', 'neighbourhood_group', 'reviews_per_month', 'number_of_reviews'])

# Step 2: Calculate Average Price by Neighborhood Group
city_avg_price = a_cleaned.groupby('neighbourhood_group')['price'].mean().sort_values(ascending=False)
print("Average Price by Neighborhood Group:")
print(city_avg_price)

# Step 3: Calculate Average Price by Property Type
type_avg_price = a_cleaned.groupby('room_type')['price'].mean().sort_values(ascending=False)
print("\nAverage Price by Property Type:")
print(type_avg_price)

# Step 4: Calculate Correlations with Review Metrics
correlation_reviews = a_cleaned['number_of_reviews'].corr(a_cleaned['price'])
correlation_monthly = a_cleaned['reviews_per_month'].corr(a_cleaned['price'])
print(f"\nCorrelation with number_of_reviews: {correlation_reviews}")
print(f"Correlation with reviews_per_month: {correlation_monthly}")

# (Optional) Step 5: Visualize the Data (requires matplotlib and seaborn)
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
sns.scatterplot(data=a_cleaned, x='reviews_per_month', y='price', hue='neighbourhood_group')
plt.title("Price vs Reviews per Month by Neighborhood Group")
plt.xlabel("Reviews per Month")
plt.ylabel("Price ($)")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()