# Author: Alex Nastase
# Created an interpolation model of Karonga Irradiance data from 2018-2021
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d


# source = https://www.ijitee.org/wp-content/uploads/papers/v8i8/H6564068819.pdf

values1 = [8.01, 7.83, 7.70, 7.08, 6.32, 5.78, 5.91, 6.26, 6.55, 7.74, 8.04, 7.16]
values2 = [8.26, 8.22, 8.03, 7.31, 6.50, 6.08, 6.11, 6.10, 6.80, 7.81, 8.17, 6.40]
values3 = [8.10, 8.72, 8.41, 7.94, 7.19, 6.34, 5.87, 6.07, 6.92, 7.57, 8.94, 8.17]
values4 = [8.83, 9.05, 8.94, 8.36, 7.34, 6.10, 5.67, 6.15, 7.16, 7.65, 9.35, 9.44]

# number of days in month so we can make sure the days are real
days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

x = np.arange(1, 13)  # Months from 1 to 12

# Interpolation function
interp_func1 = interp1d(x, values1, kind='nearest', fill_value='extrapolate',bounds_error=False)
interp_func2 = interp1d(x, values2, kind='nearest', fill_value='extrapolate',bounds_error=False)
interp_func3 = interp1d(x, values3, kind='nearest',fill_value='extrapolate',bounds_error=False)
interp_func4 = interp1d(x, values4, kind='nearest',fill_value='extrapolate',bounds_error=False)

# Interpolated X values
x_interp = np.linspace(1, 13, 100)

# Plot the original data points and the interpolated data
plt.figure(figsize=(10, 6))
plt.plot(x, values1, 'o', label='2018',color='red')
plt.plot(x_interp, interp_func1(x_interp),color='red')
plt.plot(x, values2, 'o', label='2019',color='blue')
plt.plot(x_interp, interp_func2(x_interp),color='blue')
plt.plot(x, values3, 'o', label='2020',color='green')
plt.plot(x_interp, interp_func3(x_interp),color='green')
plt.plot(x, values4, 'o', label='2021',color='orange')
plt.plot(x_interp, interp_func4(x_interp),color='orange')
def main():
    while(True):
        find_value()

# Set x-ticks and x-ticklabels
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.xticks(range(1, 13), months)
plt.yticks(np.arange(5, 12, 0.5))
plt.legend()
plt.grid(True)
plt.title('Yearlong Interpolation Model of Karonga Irradiance')
plt.xlabel('Time (months)')
plt.ylabel('Irradiance (kWh/m^2/day)')
plt.draw()
plt.savefig("quadratic_interpolation.svg")

def find_value():
    # Read a date string from standard input
    date_str = input("Please enter a date in the format MM.DD, or q,quit to quit: ")
    if(date_str == "q" or date_str == "quit"):
        exit()
    # Split the date string into month and day
    month, day = map(int, date_str.split('.'))
    if(month > 12 or month < 0):
        print("Invalid Month")
        return
    if(day > days_in_month[month] or day < 0):
        print("Invalid Day")
        return
    
    # Convert the date to a decimal number
    x_value = month + day / days_in_month[month] 
    
    # Find the interpolated value
    y_max = max(interp_func1(x_value),interp_func2(x_value),interp_func3(x_value),interp_func4(x_value))
    y_min = min(interp_func1(x_value),interp_func2(x_value),interp_func3(x_value),interp_func4(x_value))
    
    y_max = np.around(y_max, 2)
    y_min = np.around(y_min, 2)

    print("Historical Range for ",date_str, ": ",y_min,"-",y_max,"kWh/m^2/day")

plt.show()

while(True):
    find_value()
