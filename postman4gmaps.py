# geolocation

import requests
import json

url = "https://www.googleapis.com/geolocation/v1/geolocate?key=APIKEY"

payload = json.dumps({
  "macAddress:": "ac:de:48:00:11:22",
  "considerIp": "false"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)