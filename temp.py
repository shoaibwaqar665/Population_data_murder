import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Calculate the maximum and minimum difference in murder rates across countries
max_difference = df['Rate'].max() - df['Rate'].min()
min_country = df.loc[df['Rate'].idxmin(), 'Location']
max_country = df.loc[df['Rate'].idxmax(), 'Location']

print(f"Maximum difference in murder rates: {max_difference}")
print(f"Country with minimum murder rate: {min_country}")
print(f"Country with maximum murder rate: {max_country}")

# For regional analysis, group data by 'Region' and calculate mean murder rates
region_mean_rates = df.groupby('Region')['Rate'].mean().reset_index()

# Setting the visual style of the plot
sns.set_style("whitegrid")

# Creating the plot
plt.figure(figsize=(10, 6))
sns.barplot(x='Region', y='Rate', data=region_mean_rates.sort_values('Rate', ascending=False), palette='viridis')
plt.title('Mean Murder Rates by Region', fontsize=15)
plt.xlabel('Region', fontsize=12)
plt.ylabel('Mean Murder Rate (per 100,000 population)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

# Display the plot
plt.show()
