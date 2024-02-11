import json
import requests

def getAll(geocode, apikey, *reqs):
    request = f"http://geocode-maps.yandex.ru/1.x/"
    paramPamPam = {
        "geocode": geocode,
        "format": "json",
        "apikey": apikey,
    }

    response = requests.get(request, params=paramPamPam)
    
    if response.status_code == 200:
        response = response.json()
    
    else:
        return
    
    response = response["response"]["GeoObjectCollection"]["featureMember"][0]

    dictForReturning = {}
    if 'coords' in reqs:
        file = open("file.json", "w")
        json.dump(response, file)
        dictForReturning['coordinates'] = response["GeoObject"]['Point']["pos"].split()
    
    if "span" in reqs:
        crds = (response['Point']["pos"])


    return dictForReturning


