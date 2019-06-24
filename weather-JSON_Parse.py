import requests
import json
import FileHandeling

def search_countries(location):
    try:
        openCountry=open("weather.txt","r",encoding="utf8")
        readCountries=openCountry.readlines()
        countries=(FileHandeling.search_countries(readCountries,location.upper()))
        return countries
    except Exception:
        print(Exception)

res = ""
askuser = input ("enter 1 for location or 2 for lat-long:")
no_of_days=0
if int(askuser) == 1:
    asklocation = input ("Enter location:")
    no_of_days=int(input("enter no of days(1-2)"))
    result=search_countries(asklocation)
    num=1
    for country in result:
        print(str(num)+":"+country)
        num+=1
    askuser=input("Choose Location")
    newlocation=result[(int(askuser)-1)]
    user_url = ("https://www.metaweather.com/api/location/search/?query={}".format(newlocation))
    res = requests.get(user_url)

elif int (askuser) == 2:
    asllatt = str(input ("enter latt "))
    asklong = str(input ("enter long"))
    user_url = "https://www.metaweather.com/api/location/search/?lattlong={},{}".format(asllatt, asklong)
    res = requests.get (user_url)
try:
    jsonobject = json.loads (res.text)
    woeid = jsonobject [0] ["woeid"]

    woeidres = requests.get ("https://www.metaweather.com/api/location/{}/".format(woeid))
    weather = json.loads(woeidres.text)
    for i in range(no_of_days):
        weather_name = weather["consolidated_weather"][i]["weather_state_name"]
        weather_min_temp= weather["consolidated_weather"][i]["min_temp"]
        weather_max_temp = weather ["consolidated_weather"][i]["max_temp"]
        weather_current_temp = weather ["consolidated_weather"][i]["the_temp"]
        if i==0:
            day="Today"
        else:
            day="Tomorrow"
        print ("{} Weather in {} is:".format(day,newlocation))
        print("{} with\nMinimum temperature of: {} °C"
              "\nmaximum temperature of: {} °C\n"
              "Current Temperature is:{} °C"
              .format(weather_name,weather_min_temp,weather_max_temp,weather_current_temp))


except:
    print("no data found")