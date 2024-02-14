import os
import sys
import requests
from PIL import Image
# from io import BytesIO


def getmap(span=None, params=None):
    if span:
        map_request = f"http://static-maps.yandex.ru/1.x/?{span}&l=map"
    else:
        map_request = f"http://static-maps.yandex.ru/1.x/?l=map"

    if params:
        map_request += "&" + params
    response = requests.get(map_request)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)

    Image.open(map_file).show()
    os.remove(map_file)