# Working with pandas (data frames and series)
import pandas 

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))

# Python comp
average = sum(temp_list) / len(temp_list)

# With pandas data series 
print(data["temp"].mean())


