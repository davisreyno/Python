# Working with CSV data 

# Simple open and read CSV
with open("weather_data.csv") as weather_data_file:
    weather_data = weather_data_file.readlines()
    print(weather_data)


# Using CSV libary with "reader" mode
import CSV 

with open("weather_data.csv") as data_file: 
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)


# Pandas - Python data analysis library. More info on pandas.pydata.org 
import pandas 

data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])