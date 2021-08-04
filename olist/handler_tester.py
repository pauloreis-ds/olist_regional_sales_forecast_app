import requests
import json

# API Call
url = 'http://192.168.0.8:5000/olist/forecast'
# url = 'https://olist-arima-forecast.herokuapp.com/olist/forecast'
header = {'Content-type': 'application/json' }
region = json.dumps({"region":"midwest"})

r = requests.post( url, data=region, headers=header )
print( 'Status Code {}'.format( r.status_code ) )
print(r.text)