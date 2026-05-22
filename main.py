import requests
import time

URL = "https://puffzonex.com/products.json?limit=250"

def get_products():
    try:
        data = requests.get(URL).json()
        products = data["products"]

        stock = []

        for product in products:
            title = product["title"]

            available = False

            for variant in product["variants"]:
                if variant["available"]:
                    available = True

            if available:
                stock.append(title)

        return stock

    except Exception as e:
        return [f"Fejl: {e}"]

while True:
    products = get_products()

    print("\n🔥 PÅ LAGER 🔥\n")

    for item in products[:20]:
        print(item)

    time.sleep(60)
