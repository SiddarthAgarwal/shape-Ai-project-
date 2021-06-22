import requests
import decimal
#import os
from datetime import datetime
api_key = 'aad5ff1761af1a2a110b14ac0a8d4bd3'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")
print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')
decimal.getcontext().prec=4
temperature=decimal.Decimal(temp_city)+0


# started writing in file

f1=open("Weather_report.txt","a")
f1.write("-------------------------------------------------------------")
f1.write("\n")
f1.write("Weather Stats for     : ")
f1.write(str(location.upper()) )
f1.write("\t") 
f1.write(str(date_time))
f1.write("\n")
f1.write("-------------------------------------------------------------")
f1.write("\n")
f1.write("Current temperature is: ")
f1.write(str(temperature))
f1.write(" deg C")
f1.write("\n")
f1.write("Current weather desc  : ")
f1.write(weather_desc)
f1.write("\n")
f1.write("Current Humidity      : ")
f1.write(str(hmdt))
f1.write(" %")
f1.write("\n")
f1.write("Current wind speed    : ")
f1.write(str(wind_spd))
f1.write(" kmph")
f1.write("\n")
f1.write("\n")
f1.flush()
f1.close()


