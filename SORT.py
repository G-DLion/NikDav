import getUrl as GU
from operator import itemgetter

def ssort(x):
    return x['price']

def unpack(data):
    price_data = []
    name_data = []
    data.sort(key=lambda x: str(x['price']))
    for exchange in data:
        for key, value in exchange.items():
            if key == 'price':
                price_data.append(float(value))
            elif key == 'name':
                name_data.append(str(value))
    print(price_data)
    print(name_data)

while True:
    exchanges = GU.get_data('Binance','USDT',100)
    unpack(exchanges)
