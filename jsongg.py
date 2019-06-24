import requests
import json

askuser=input("enter 1 for location or 2 for lat-long:")
if int(askuser)==1:
    asklocation=input("Enter location:")
    user_url = ("https://www.metaweather.com/api/location/search/?query={}".format(asklocation))
    res = requests.get(user_url)

elif int(askuser)==2:
    asllatt=input("enter latt ")
    asklong=input("enter long")
    user_url="https://www.metaweather.com/api/location/search/?lattlong=({]),({])".format(asllatt,asklong)
    res = requests.get(user_url)

jsonobject=json.loads(res.text)
print(jsonobject[0])
woeid=jsonobject[0]["woeid"]

woeidres=requests.get("https://www.metaweather.com/api/location/{}/".format(woeid))
weather=json.loads(woeidres.text)
weather_name=weather["consolidated_weather"][0]["weather_state_name"]

print(weather_name)



