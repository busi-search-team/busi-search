#import db.py
from collections import Counter
import requests
from lxml import html
import csv
#import maps.py

'''def fetch_busi(location) :
    #create csv
    #record every name, id, website

    allowed_types = [] #location types that can be small businesses

    with open('locations.csv', 'w+', newline='') as csvfile:
        fieldnames = ['place_id', 'url', 'name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for a in googlemaps thing luist:
            if a.type in allowed_types: writer.writerow({'place_id': a.x, 'url': a.y, 'name': a.z})'''



def filter_small(locations, output) :
    d = {}

    with open(locations, 'r', encoding='utf-8') as inp:
        for row in csv.reader(inp):
            # if we have not seen team before, create k/v pairing
            # setting value to 0, if team already in dict this does nothing
            d.setdefault(row[1],0)
            print(row[1])
            # increase the count for the team
            d[row[1]] += 1

    with open(locations, 'r', encoding='utf-8') as inp, open(output, 'w', newline='', encoding='utf-8') as out:  
        writer = csv.writer(out)

        for row in csv.reader(inp):
            print('plz work')
            #iterates through all urls, deletes duplicates exceeding x
            if d[row[1]] < 3 or row[1] == 'facebook.com': 
                writer.writerow(row)
            print(f"test {d[row[1]]}")
        for key, count in d.items():
            print("{} {}".format(key,count))


    #return new

dict = {1 : "man", 2: "guy", 3: "man", 4: "female"}
dict2 = {2: "guy", 3: "manor"}
#print(filter_small(1, 2))
filter_small('new.csv', 'output.csv')


