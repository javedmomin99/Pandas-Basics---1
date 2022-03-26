import pandas
# titanic = pandas.read_csv("C:/Users/javed/Downloads/titanic_dataset.csv")
# Converting to a DataFrame by specifying Specific Columns in the form of a List which we need to Analyse
# data = pandas.DataFrame(titanic)
# print(data)
import requests
response = requests.get(url="https://api.github.com/repos/pandas-dev/pandas/issues")
json = response.json()
#print(len(json))
#Find Title of All Issues
#for i in range(len(json)):
#    print(json[i]["title"])

# Using Pandas Doing the Same Thing as Above:
#Find URL & Title of All Issues : 
#URL_Title =pandas.DataFrame(json,columns=["url"])

data = pandas.DataFrame(json)
print(data)
data.to_csv("C:/Users/javed/Desktop/pandas/dump_data.csv")

#print(URL_Title)
#print(All_Data)
json_reader = pandas.read_json("https://api.github.com/repos/pandas-dev/pandas/issues")
print(json_reader)
