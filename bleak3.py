# usr info

import requests
import platform 

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "latitude": response.get("latitude"),
        "longitute": response.get("longitude"),
        "postal": response.get("postal"),
        "hostname": response.get("hostname")
    }
    return location_data


print(get_location())
# prints the name of a device
print('Device name:',platform.node())