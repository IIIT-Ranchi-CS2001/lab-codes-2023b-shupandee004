#Q2
import pandas as pd
file_path = 'AQI_Data.csv'
data = pd.read_csv(file_path)

if 'City' in data.columns and 'PM2.5' in data.columns:
    grouped_data = data.groupby('City').agg({     
        'PM2.5': 'max'       
    }).reset_index()

    grouped_data.rename(columns={'PM2.5': 'Maximum PM2.5'}, inplace=True)

    print(grouped_data)
else:
    print("The required columns ('City', 'AQI', 'PM2.5') are not present in the data.")