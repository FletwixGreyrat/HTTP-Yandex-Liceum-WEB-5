import sys
from viev import getmap
from geocoder import getAll

apiKey = "7d42a436-37e1-41f5-b92a-c61cca026788"

def search():
    toponym_to_find = " ".join(sys.argv[1:])

    if toponym_to_find:
        l1, l2 = getAll(toponym_to_find, apiKey, "coords")["coordinates"]
        span = f"ll={l1},{l2}&spn=0.005,0.005"
        getmap(span,)

        ll, span = getmap(toponym_to_find)
        span = f"ll={ll}&spn={span}"
        getmap(span, ll_spn=0.005)

        point_param = f"pt={ll}"
        getmap(span, add_params=point_param)


if __name__ == "__main__":
    search()