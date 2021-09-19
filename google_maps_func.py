from typing import Counter
import requests
from geopy.geocoders import Nominatim
import json
import time
import csv
import re
from urllib.request import urlopen
from urllib.parse import urlparse
'''#User types their city
user_loc = input("Enter your city: ")
geolocater = Nominatim(user_agent = 'e')
#Finds user location based on their city (latitude and longitude)
location = geolocater.geocode(user_loc)
#User inputs a keyword that will dictate their search results
user_interest = input("Interest: ")
#print(location.latitude, location.longitude)'''

def get_hostname(url, uri_type='both'):
    """Get the host name from the url"""
    parsed_uri = urlparse(url)
    n_url = '{uri.netloc}'.format(uri=parsed_uri)
    if n_url.startswith('www.'):
        n_url = re.sub(r'www.', '', n_url)
    return n_url

#Url uses the api and formats link to a "nearby places" search result on Google Maps
#url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={}%2C{}&radius=25000&keyword={}&key=AIzaSyA8QxuHEGCsKOcdsAAdNK7BHR7HIJWxNa4".format(location.latitude, location.longitude, user_interest)
#Gets the HTTP request
place_details = []
place_ids = []
def get_info(url, csv_enable='', category='') :
    all_types = ["bakery","bar","beauty_salon","book_store","convenience_store",
"florist","food","grocery_or_supermarket","hair_care","laundry","movie_theater","night_club","painter","plumber","restaurant"
"roofing_contractor","spa","supermarket","veterinary_care"]
    if csv_enable != '':
        csvfile = open(csv_enable, 'a', newline='', encoding="utf-8")
        fieldnames = ['place_id', 'url', 'name', 'latitude', 'longitude', 'category']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    global place_details
    payload = {}
    headers = {}
    #global response
    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        global json_data
        json_data = response.json()
    except Exception as e:
        print(e)
    for r in range(0,20):
        try:
            stat = json_data["results"][r]["name"]
        except:
            break
        p_id = json_data["results"][r]["place_id"]
        place_ids.append(p_id)
        lat = json_data["results"][r]["geometry"]["location"]["lat"]
        lng = json_data["results"][r]["geometry"]["location"]["lng"]
        place_details.append(p_id)
        link = "https://maps.googleapis.com/maps/api/place/details/json?place_id={}&fields=website%2Ctype%2Cvicinity&key=AIzaSyA8QxuHEGCsKOcdsAAdNK7BHR7HIJWxNa4".format(place_details[len(place_details)-1])
        payload={}
        headers = {}
        detail_response = requests.request("GET", link, headers=headers, data=payload)
        detail_json = detail_response.json()
        print(link)
        try:
            site = get_hostname(detail_json["result"]["website"], 'netloc_only')
            _type = detail_json["result"]["types"]
            print("NAME:", stat)
            print("place_id: ", p_id)
            print("site:", site)
            for i in range(len(_type)):
                print("type", i, ": ", _type[i])
                
            if csv_enable != '':
                if _type[0] in all_types or _type[1] in all_types:
                    writer.writerow({'place_id': p_id, 'url': site, 'name': stat, 'latitude': lat, 'longitude': lng, 'category': category})
        except Exception as e:
            print(e)
    try:
        return "https://maps.googleapis.com/maps/api/place/nearbysearch/json?pagetoken={}&key=AIzaSyA8QxuHEGCsKOcdsAAdNK7BHR7HIJWxNa4".format(json_data["next_page_token"])
    except:
        return ""

def api_search(location, cat):
    return "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={}%2C{}&radius=25000&keyword={}&key=AIzaSyA8QxuHEGCsKOcdsAAdNK7BHR7HIJWxNa4".format(location.latitude, location.longitude, cat)

#huh = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={}%2C{}&radius=25000&key=AIzaSyA8QxuHEGCsKOcdsAAdNK7BHR7HIJWxNa4".format(location.latitude, location.longitude)

#print("HUH:", huh)
def find_from_id(place_id):
    link = "https://maps.googleapis.com/maps/api/place/details/json?place_id={}&fields=website%2Ctype%2Cvicinity&key=AIzaSyA8QxuHEGCsKOcdsAAdNK7BHR7HIJWxNa4".format(place_details[len(place_details)-1])
    payload={}
    headers = {}
    detail_response = requests.request("GET", link, headers=headers, data=payload)
    json_data = detail_response.json()
    print(json_data["results"]["name"])
    print(json_data["results"]["rating"])
    print(json_data["results"]["photos"]["html_attributions"])
        



def init_csv(output):
    csvfile = open(output, 'w', newline='')
    csvfile.write('')
    fieldnames = ['place_id', 'url', 'name', 'latitude', 'longitude', 'category']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    csvfile.close()

def fetch_maps(location, search, category, output):
    huh = api_search(location, search)
    for i in range(3):
        huh = get_info(huh, output, category)
        print("HUH:", huh)
        time.sleep(2)

find_from_id('ChIJmzrzi9Y0K4gRgXUc3sTY7RU')