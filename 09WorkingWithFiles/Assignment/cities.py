import json
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

f = open("../data/1000-largest-us-cities.json", "r")
cities = json.load(f)
f.close()
kasas_cities = []
for city in cities:
    if city["state"] == "Kansas":
        kasas_cities.append(city["city"])
print("The Kansas Cities are:", kasas_cities)

current_longest_name = "a"
for city in cities:
    if len(city["city"]) >= len(current_longest_name):
        current_longest_name = city["city"]
print("The City With the Longest Name is:", current_longest_name)

biggest_latitude = -999999999999999999999999999999
smallest_latitude = 999999999999999999999999999999
biggest_longitude = -999999999999999999999999999999
smallest_longitude = 999999999999999999999999999999
biggest_latitude_name = ""
smallest_latitude_name = ""
biggest_longitude_name = ""
smallest_longitude_name = ""
for city in cities:
    if city["latitude"] >= biggest_latitude:
        biggest_latitude = city["latitude"]
        biggest_latitude_name = city["city"]
    if city["latitude"] <= smallest_latitude:
        smallest_latitude = city["latitude"]
        smallest_latitude_name = city["city"]
    if city["longitude"] >= biggest_longitude:
        biggest_longitude = city["longitude"]
        biggest_longitude_name = city["city"]
    if city["longitude"] <= smallest_longitude:
        smallest_longitude = city["longitude"]
        smallest_longitude_name = city["city"]
print("The Most Nothern City is:", biggest_latitude_name)
print("The Most Southern City is:", smallest_latitude_name)
print("The Most Eastern City is:", biggest_longitude_name)
print("The Most Western City is:", smallest_longitude_name)

biggest_growth = -999999999
biggest_growth_name = ""
smallest_growth = 999999999
smallest_growth_name = ""
for city in cities:
    if city["growth_from_2000_to_2013"] == "":
        growth = 0
    else:
        growth = float(city["growth_from_2000_to_2013"].strip("%"))
    if growth >= float(biggest_growth):
        biggest_growth_name = city["city"]
        biggest_growth = growth
    if growth <= float(smallest_growth):
        smallest_growth_name = city["city"]
        smallest_growth = growth
print("The City With the Biggest Growth from 2000-2013 is:", biggest_growth_name)
print("The City With the Biggest Shrinkage from 2000-2013 is:", smallest_growth_name)
