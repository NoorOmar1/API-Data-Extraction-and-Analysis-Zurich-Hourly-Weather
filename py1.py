import requests 
import pandas as pd 


url = 'https://api.open-meteo.com/v1/forecast?latitude=47.37&longitude=8.55&hourly=temperature_2m,rain,snowfall,snow_depth,is_day&models=meteoswiss_icon_ch1'

#Location: Zurich, Switzerland 
params = {
    "latitude": 47.37,
    "longitude": 8.55,
    "hourly": "temperature_2m,rain,snowfall,snow_depth,is_day",
    "models": "meteoswiss_icon_ch1"
}

# checking the connection and type of data: 
'''
response = requests.get(url, params = params)
if response.status_code == 200:
    data = response.json()
    print('success')
    print(type(data))
    print(data[:2])
else:
    print('something went wrong') '''
###################################
response = requests.get(url, params = params)

if response.status_code == 200:
    data = response.json()
    print("✅ Data fetched successfully!")

    # Extract hourly data section
    hourly_data = data[0]['hourly']

    # Create a pandas DataFrame
    df = pd.DataFrame(hourly_data)

    # Rename columns for clarity
    df.rename(columns={
        "temperature_2m_meteoswiss_icon_ch1": "Temperature (°C)",
        "rain_meteoswiss_icon_ch1": "Rain (mm)",
        "snowfall_meteoswiss_icon_ch1": "Snowfall (cm)",
        "snow_depth_meteoswiss_icon_ch1": "Snow Depth (m)",
        "is_day_meteoswiss_icon_ch1": "Is Day"
    }, inplace=True)

    
    print(df.head())

else:
    print("Error fetching data:", response.status_code)


#importing to Excel
excel_file = r"C:\Users\20111\Desktop\Pandas project 1\py1_data.xlsx"
df.to_excel(excel_file, index=False, sheet_name = 'weather_data')
print('Saved to excel')



