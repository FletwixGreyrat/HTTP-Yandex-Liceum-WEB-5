import sys
from viev import getmap
from geocoder import getAll, getLocation, lld

apiKey1 = "7d42a436-37e1-41f5-b92a-c61cca026788"
apiKey2 = "c4e6b229-cb0b-42cb-b3b5-ce2a2e6f85a0"
span = "0.005,0.005"

if __name__ == "__main__":
    toponym = ' '.join(sys.argv[1:])
    coords = ",".join(getAll(toponym, apiKey1, "coords")["coordinates"])
    apteka = getLocation(apiKey2, coords, span, "атпека")
    l1, l2 = [float(i) for i in apteka["geometry"]["coordinates"]]
    param = f"pt={l1},{l2},pm2dgl"
    # getmap(f"ll={coords}&spn={span}", params=param)
    params = param + f"~{coords},pm2rdl"
    # getmap("ll={0}&spn={1}".format(coords, span), params=params)
    getmap(params=params)

    name = apteka["properties"]["CompanyMetaData"]["name"]
    address = apteka["properties"]["CompanyMetaData"]["address"]
    time = apteka["properties"]["CompanyMetaData"]["Hours"]["text"]
    distance = round(lld((coords.split(",")[1], coords.split(",")[0]), (l2, l1)))

    snippet = f"Название:\t{name}\nАдрес:\t{address}\nВремя работы:\t{time}\n" \
              f"Расстояние:\t{distance}м."
    print(snippet)