import json
import math
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
        dictForReturning['coordinates'] = response["GeoObject"]['Point']["pos"].split()
    
    if "span" in reqs:
        crds = (response['Point']["pos"])


    return dictForReturning


def getLocation(apiKey, ll, spn, request):
    req = "https://search-maps.yandex.ru/v1/"
    params = {
        "apikey": apiKey,
        "text": request,
        "lang": "ru_RU",
        "ll": ll,
        "spn": spn,
        "type": "biz"
    }

    response = requests.get(req, params=params).json()
    file = open("file.json", "w")
    json.dump(response, file)
    return response["features"]


def lld(a, b):
    zxc = 111 * 1000
    a1, a2 = a
    b1, b2 = b
    bankai = math.radians((float(a2) + float(b2)) / 2.)
    cursed = math.cos(bankai)
    dx = abs(float(a1) - float(b1)) * zxc * cursed
    dy = abs(float(a2) - float(b2)) * zxc
    distance = math.sqrt(dx * dx + dy * dy)

    return distance