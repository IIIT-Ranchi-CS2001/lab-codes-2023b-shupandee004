#common Question
import pandas as pd
import numpy as np


df = pd.read_csv('AQI_Data.csv')


print("First 8 rows of the dataset:")
print(df.head(8))


print("\nLast 5 rows of the dataset:")
print(df.tail(5))


selected_columns = df[['City', 'AQI', 'PM2.5', 'PM10']]
grouped = selected_columns.groupby('City')
result = grouped.mean()



print(result)


average_aqi = df['AQI'].mean()
print(f"The average AQI is: {average_aqi}")

max_pm2_5=df['PM2.5'].max()
print(f"The minimum PM2.5 level is: {max_pm2_5}")

min_pm10 = df['PM10'].min()
print(f"The minimum PM10 level is: {min_pm10}")

print("\n")
print(df.info())

result.to_csv('pivot.csv', index=True)