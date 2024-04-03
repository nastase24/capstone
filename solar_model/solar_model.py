# Solar Radiance Model Using the Malawi Weather Tower Data
# Name: Alexander Nastase

import numpy as np
import glob
import pandas as pd
from datetime import datetime as dt
import matplotlib.pyplot as plt

# Read in the Weather Data, catching any errors
# get the path of the weather data
# NOTE: if not in the same directory as solar_model.py, update this path
path = glob.glob("./ambient-weather*.csv")
try:
    weather_data = pd.concat(pd.read_csv(file,usecols=[1,16], names=["Time","Radiation"],skiprows=[0]) for file in path)
    #print(weather_data)
except: 
    print("Error reading in weather data")
    exit()

#print(weather_data)
#print(weather_data.columns)
#monthly_data = weather_data.resample('M').agg({'Radiation': ['min', 'max']}).dropna()
#monthly_data['Radiation', 'avg'] = [6.32, 5.78, 5.91, 6.26, 6.55, 7.74]

#Format the Data
#2023-10-03 20:27:00 is in the format YYYY-MM-DD HH:MM:SS. Goal: HHMM
weather_data.Time = pd.to_datetime(weather_data.Time,format='%Y-%m-%d %H:%M:%S').dt.strftime('%H%M').astype(int)
print(weather_data)
#Calculate stats of the dataset
#calculate the mean, median, mode, and range of the Radiation column
mean = round(weather_data['Radiation'].mean(), 2)
median = round(weather_data['Radiation'].median(), 2)
mode = round(weather_data['Radiation'].mode()[0], 2)
max = round(weather_data['Radiation'].max(), 2)
min = round(weather_data['Radiation'].replace(0,np.nan).min(), 2)
stdev = round(weather_data['Radiation'].std(), 2)
time_of_peak = weather_data.at[weather_data['Radiation'].idxmax(), 'Time']
print(time_of_peak)
print(f"Mean: {mean}, Median: {median}, Mode: {mode}, Max: {max}, Min: {min}, Stdev: {stdev} Time of Peak: {time_of_peak} W/m^2")

#writing the stats to a file
# with open('stats.txt', 'w') as file:
#     file.write(f"Mean: {mean}, Median: {median}, Mode: {mode}, Max: {max}, Min: {min}, Stdev: {stdev} Time of Peak: {time_of_peak} W/m^2")

# Plot the boxplot on the first axis


# Plot the scatterplot on the second axis
plt.scatter(weather_data.Time, weather_data.Radiation)
#plt.plot(x, quadratic(x), color='red')
plt.title("24-hour Solar Radiation Model: 5.18.23-11.07.23")
plt.xlabel("Time (24-hr clock)")
plt.ylabel("Solar Radiation (W/m^2)")
plt.savefig("24 Hour Solar Radiation Model.svg")
# Show the plots
plt.show()

