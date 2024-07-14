# with open("weather_data.csv") as file_data:
#     data = file_data.readlines()
#
# print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data.temp.max())
#
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# print((monday_temp * 1.8) + 32)

# # create data frame
# data_dict = {
#     "students": ["amy", "gerald", "ibby"],
#     "scores": [65, 76, 98],
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# # converting to csv file
# data.to_csv("new_data.csv")

import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240714.csv")
gray_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])
black_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
cinnamon_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
print(gray_squirrels_count)
print(black_squirrels_count)
print(cinnamon_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count],
}

df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_counts.csv")

