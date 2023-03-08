# geolocation

import requests
import json

url = "https://www.googleapis.com/geolocation/v1/geolocate?key=APIKEY"

payload = json.dumps({
  "macAddress:": "INSERT",
  "considerIp": "false"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

# response body(postman)

{
  "macAddress:": "INSERT",
  "considerIp": "false"

}