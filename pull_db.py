from geopy.geocoders import Nominatim
import json
import time
import csv
import google_maps_func

#user_loc = input("Enter your city: ")
geolocater = Nominatim(user_agent = 'e')
#Finds user location based on their city (latitude and longitude)
location = [geolocater.geocode('Toronto'), geolocater.geocode('Montreal')]

place_details = []
searches = {
    'thai food': 'Southeast Asian Restaurant',
    'viatnamese food':'Southeast Asian Restaurant',
    'japanese food': 'East Asian Restaurant',
    'chinese food': 'East Asian Restaurant',
    'korean food' : 'East Asian Restaurant',
    'arabic food' : 'Middle Eastern Restaurant',
    'persian food': 'Middle Eastern Restaurant',
    'italian food' : 'Italian Restaurant',
    'mexican food' : 'Mexican Restaurant',
    'indian food' : 'Indian Restaurant',
    'restaurant' : 'Restaurant',
    'cafe' : 'Cafe',
    'supermarket' : 'Supermarket',
    'shoes' : 'Shoes',
    'convenience store' : 'Convenience Store',
    'bakery' : 'Bakery',
    'vet' : 'Vetrinarian Clinic',
    'laundry' : 'Laundry',
    'appliances' : 'Appliance Stores',
    'hair cut' : 'Hair Salon',
    'nail salon' : 'Nail Salon',
    'spa' : 'Spa'}

out_csv = 'new.csv'

google_maps_func.init_csv(out_csv)

for search, cat in searches.items():
    for i in range(len(location)):
        google_maps_func.fetch_maps(location[i], search, cat, out_csv)