import requests

MY_LAT = 39.952583
MY_LONG = -75.165222
#------------------------ISS-Location-------------------------#
# response = requests.get('http://api.open-notify.org/iss-now.json')
# response.raise_for_status()
#
# data = response.json()
#
# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']
#
# iss_position = (longitude, latitude)
# print(f'Current ISS position is: {iss_position}')

parameters = {
	"lat": MY_LAT,
	"lng":MY_LONG
}
#-------------------------- WiTHOUT Paremeters---------------------------------#
response = requests.get('https://api.sunrise-sunset.org/json')
response.raise_for_status()
data = response.json()
print(data)
#-------------------------- WiTH Paremeters---------------------------------#
response = requests.get('https://api.sunrise-sunset.org/json',params=parameters)
response.raise_for_status()
data2 = response.json()
print(data2)
#-------------------------- Formatted turned off ---------------------------------#
parameters = {
	"lat": MY_LAT,
	"lng":MY_LONG,
	"formatted":0
}
response = requests.get('https://api.sunrise-sunset.org/json',params=parameters)
response.raise_for_status()
data3 = response.json()
print(data3)