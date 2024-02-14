import sys
from viev import getmap
from geocoder import getAll, getLocation

apiKey1 = "7d42a436-37e1-41f5-b92a-c61cca026788"
apiKey2 = "c4e6b229-cb0b-42cb-b3b5-ce2a2e6f85a0"
span = "0.005,0.005"

if __name__ == "__main__":
    toponym = " ".join(sys.argv[1:])

    address = ",".join(getAll(toponym, apiKey1, "coords")["coordinates"])

    orgs = []
    spn = 0.01
    while not (spn >= 100) and not (len(orgs) >= 10):
        spn *= 2.0
        span = f"{spn},{spn}"
        orgs = getLocation(apiKey2, address, span, "аптека")

    lst = []
    for i in orgs:
        zxc = i["geometry"]["coordinates"]
        hours = i["properties"]["CompanyMetaData"].get("Hours", None)
        if hours:
            available = hours["Availabilities"][0]
            is_24x7 = available.get("Everyday", False) and available.get("TwentyFourHours", False)
        else:
            is_24x7 = None
        lst.append((zxc, is_24x7))

    params = "pt=" + "~".join([f'{zxc[0]},{zxc[1]},pm2{"gn" if is_24x7 else ("lb" if not is_24x7 else "gr")}l' for zxc, is_24x7 in lst])
    getmap(params=params)