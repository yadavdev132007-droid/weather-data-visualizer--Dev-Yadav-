import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------
# Task 1: Load Data
# ------------------------
df = pd.read_csv("weather.csv")   # <-- put your CSV name here
df['Date'] = pd.to_datetime(df['Date'])

print(df.head())
print(df.info())
print(df.describe())

# ------------------------
# Task 2: Clean Data
# ------------------------
df = df[['Date', 'Temp', 'Rain', 'Humidity']].copy()

df['Temp'] = pd.to_numeric(df['Temp'], errors='coerce')
df['Rain'] = pd.to_numeric(df['Rain'], errors='coerce')
df['Humidity'] = pd.to_numeric(df['Humidity'], errors='coerce')

df.fillna(method="ffill", inplace=True)

df.set_index('Date', inplace=True)

# ------------------------
# Task 3: NumPy Statistics
# ------------------------
daily_mean = np.mean(df['Temp'])
monthly_stats = df['Temp'].resample('M').agg(['mean','min','max','std'])
yearly_stats = df['Temp'].resample('Y').agg(['mean','min','max','std'])

print("\nDaily mean temperature:", daily_mean)
print("\nMonthly stats:\n", monthly_stats)
print("\nYearly stats:\n", yearly_stats)

# ------------------------
# Task 4: Visualizations
# ------------------------

# Line chart: daily temperature
df['Temp'].plot(figsize=(10,4), title="Daily Temperature")
plt.savefig("temp_daily.png")
plt.close()

# Bar chart: monthly rainfall
df['Rain'].resample('M').sum().plot(kind='bar', figsize=(10,4), title="Monthly Rainfall")
plt.savefig("rain_monthly.png")
plt.close()

# Scatter: humidity vs temperature
df.plot(kind='scatter', x='Temp', y='Humidity', title="Humidity vs Temp")
plt.savefig("humidity_vs_temp.png")
plt.close()

# ------------------------
# Task 5: Grouping
# ------------------------
monthly_group = df.groupby(df.index.month).mean()
print("\nGrouped by Month:\n", monthly_group)

# ------------------------
# Task 6: Export
# ------------------------
df.to_csv("cleaned_weather.csv")

with open("report.md", "w") as f:
    f.write("# Weather Report\n")
    f.write("Daily, monthly and yearly weather patterns analyzed.\n")
    f.write("\n## Key Insights\n")
    f.write(f"- Daily average temperature: {daily_mean:.2f}\n")
    f.write("- See PNG images for all plots.\n")

print("\nDone! Files created:")
print("cleaned_weather.csv, temp_daily.png, rain_monthly.png, humidity_vs_temp.png, report.md")
