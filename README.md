API Integration: Used the requests library to manage HTTP requests and successfully connect with the Open-Meteo API.

Data Transformation (JSON to DataFrame): Employed pandas to parse and convert nested JSON structures into a clean, tabular DataFrame.

Data Cleaning & Preparation: Renamed cryptic API-specific keys (e.g., temperature_2m_meteoswiss_icon_ch1) into standardized, user-friendly columns.

Data Loading & Persistence: Utilized the pandas.to_excel() method with the openpyxl engine to export the final dataset.

Error Handling: Implemented status code checks to ensure data is only processed upon a successful API response.
