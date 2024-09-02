# with open("weather_data.csv") as weather_data_file:
#     weather_data = weather_data_file.readlines()
#     print(weather_data)

# Using CSV libary with "reader" mode

import CSV 

with open("weather_data.csv") as data_file: 
    data = csv.reader(data_file)
    temperatures = []
    for row in data
    p   rint(row)