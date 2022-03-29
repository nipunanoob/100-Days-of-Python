# # import csv
# #
# # with open("weather_data.csv") as file:
# #     data = csv.reader(file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] == 'temp':
# #             continue
# #         temperatures.append(int(row[1]))
# #     print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(type(data['temp']))
# #
# # data_dict = data.to_dict()
# # temp_list = data['temp'].to_list()
# # # print(data_dict)
# # print(temp_list)
# #
# # average = sum(temp_list) / len(temp_list)
# # print(average)
# #
# # print(data['temp'].mean())
#
# # print(data[data["temp"] == data["temp"].max()])
#
#
# def celsius_to_fahrenheit(temp):
#     return (temp * 9/5) + 32
#
#
# monday = data[data.day == 'Monday']
# print(celsius_to_fahrenheit(monday.temp))
#


# Get count of each fur color of squirrel

import pandas as pd

#  Converted squirrel data into a dataframe containing frequency of fur color
squirrel_data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
squirrel_fur = squirrel_data['Primary Fur Color']
squirrel_count = squirrel_fur.value_counts()
squirrel_df = squirrel_count.to_frame().reset_index()
squirrel_df.columns = ['Fur Color', 'Count']

squirrel_df.to_csv('squirrel_count.csv')



