import random
from geocoder import getAll
from viev import getmap

apiKey = "7d42a436-37e1-41f5-b92a-c61cca026788"

if __name__ == "__main__":
    cities = [
            "Ярославль",
            "Нижний Тагил",
            "Казань",
            "Великий Новгород",
            "Архангельск",
            "Саратов",
            "Петрозаводск",
            "Астрахань"
        ]
    random.shuffle(cities)

    for city in cities:
        ll, spn = getAll(city, apiKey, "span")["llspan"]
        if random.random() > 0.5:
            spn = "0.001,0.001"
            map_type = "map"
        ll_spn = f"ll={ll}&spn={spn}"
        getmap(ll_spn)