
import requests
import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


trains = "nqrw"
url = f'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-{trains}'
headers = {'content-type': 'application/json','x-api-key': 'VOmH9M2lMi5LcbcLaLY385xSuRQIwRxc3hZAJMe5'}

req = requests.get(url, headers=headers)

# jprint(req.json())

print(req.json())

# print(req.encoding)
print(f"Status code: {req.status_code}")
