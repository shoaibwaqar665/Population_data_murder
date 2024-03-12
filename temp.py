import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Calculating statistics for text information in the plot
max_difference = df['Rate'].max() - df['Rate'].min()
min_country = df.loc[df['Rate'].idxmin(), 'Location']
max_country = df.loc[df['Rate'].idxmax(), 'Location']
highest_avg_rate_region = df.groupby('Region')['Rate'].mean().idxmax()
lowest_avg_rate_region = df.groupby('Region')['Rate'].mean().idxmin()

# Preparing data for trend analysis
brazil_trend = df[df['Location'] == 'Brazil'].sort_values('Year')
japan_trend = df[df['Location'] == 'Japan'].sort_values('Year')
region_mean_rates = df.groupby('Region')['Rate'].mean().reset_index()

# Creating the figure and axes for the plots
plt.figure(figsize=(20, 18))

# Mean murder rates by region
plt.subplot(3, 2, 1)
sns.barplot(x='Region', y='Rate', data=region_mean_rates.sort_values('Rate', ascending=False), palette='viridis')
plt.title('Mean Murder Rates by Region', fontsize=15)
plt.xlabel('Region', fontsize=12)
plt.ylabel('Mean Murder Rate (per 100,000 population)', fontsize=12)
plt.xticks(rotation=45)

# Trend analysis for Brazil and Japan
plt.subplot(3, 2, 2)
sns.lineplot(x='Year', y='Rate', data=brazil_trend, marker='o', color='red', label='Brazil')
sns.lineplot(x='Year', y='Rate', data=japan_trend, marker='o', color='blue', label='Japan')
plt.title('Murder Rate Trend for Selected Countries', fontsize=15)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Murder Rate (per 100,000 population)', fontsize=12)
plt.legend()
plt.xticks(rotation=45)

# Insights text
plt.subplot(3, 2, 3)
plt.axis('off')
plt.text(0, 0.85, f"Maximum difference in murder rates: {max_difference}", fontsize=12)
plt.text(0, 0.70, f"Country with minimum murder rate: {min_country}", fontsize=12)
plt.text(0, 0.55, f"Country with maximum murder rate: {max_country}", fontsize=12)
plt.text(0, 0.40, f"Region with the highest average murder rate: {highest_avg_rate_region}", fontsize=12)
plt.text(0, 0.25, f"Region with the lowest average murder rate: {lowest_avg_rate_region}", fontsize=12)

# Relationship between murder rate and counts
plt.subplot(3, 2, 4)
sns.scatterplot(x='Rate', y='Count', data=df, hue='Region', style='Region', palette='bright')
plt.title('Assumed Relationship Between Murder Rate and Counts', fontsize=15)
plt.xlabel('Murder Rate (per 100,000 population)', fontsize=12)
plt.ylabel('Murder Count', fontsize=12)

plt.tight_layout()
plt.show()
