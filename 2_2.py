import sys
import requests
from geocoder import getAll

apiKey = "7d42a436-37e1-41f5-b92a-c61cca026788"

if __name__ == "__main__":
    try:
        toponym = " ".join(sys.argv[1:])
    except:
        exit(1)

    if not toponym:
        exit(1)

    PlaceCoords = getAll(toponym, apiKey, "coords")["coordinates"]

    ll = "{0},{1}".format(PlaceCoords[0], PlaceCoords[1])
    request = f"http://geocode-maps.yandex.ru/1.x/"
    params = {
        "apikey": apiKey,
        "geocode": ll,
        "kind": "district",
        "format": "json"}
    
    response = requests.get(request, params=params).json()

    features = response["response"]["GeoObjectCollection"]["featureMember"]
    print(features[0]["GeoObject"]["name"] if features else None)