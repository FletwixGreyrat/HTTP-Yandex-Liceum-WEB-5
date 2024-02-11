import requests
from PIL import Image
from io import BytesIO


def getmap(spn=None, **params):
    if spn:
        request = f"http://static-maps.yandex.ru/1.x/?{spn}&l=map"
    else:
        request = f"http://static-maps.yandex.ru/1.x/?l=map"
    
    keys = params.keys()
    if len(params) > 0:
        response = requests.get(request)
    else:
        response = requests.get(request, params=params)
    Image.open(BytesIO(response.content)).show()
