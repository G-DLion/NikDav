import requests

#метод для букв, делает их маленькими
def lowercase_string(string):
    return string.lower()

#создаём словарь для каждой биржи
binance_date = {}
bybit_date = {}
huobi_data = {}
bkex_data = {}
okx_data = {}
kucoin_data = {}

page_exchange = { # api для запросов
        'Binance': 'https://api.binance.com/api/v3/ticker/price?symbol=',
        'Bybit': 'https://api.bybit.com/v5/market/tickers?category=inverse&symbol=',
        'Huobi': 'https://api.huobi.pro/market/detail/merged?symbol=',
        'OKX': 'https://aws.okx.com/api/v5/market/index-tickers?instId=',
        'KuCoin': 'http://api.kucoin.com/api/v1/market/orderbook/level1?symbol=',
        'BKEX': 'https://api.bkex.com/v2/q/tickers?symbol=',
    }

list_crypto = ['BTC', 'ETH'] # валюта

def get_data(mainExchange, baseActive, balance):
    mainExchange = mainExchange.lower()

    resultArray = []

    for sym in list_crypto:
        for name_exchange, url in page_exchange.items():
            if name_exchange == 'Huobi': #получение данных с Huobi
                responses = requests.get(url + lowercase_string(sym + baseActive)).json()
                huobi_data['name'] = name_exchange
                huobi_data['price'] = price
                huobi_data['symbol'] = sym + baseActive
                if 'huobi' in mainExchange:
                    huobi_data['attrib'] = True
                    resultArray.append(huobi_data)
                else:
                    huobi_data['attrib'] = False


            elif name_exchange == 'BKEX': #получение данных с BKEX
                responses = requests.get(url + sym + '_' + baseActive).json()
                if name_exchange == 'BKEX':
                    price = responses['data'][0]['close']
                    bkex_data['name'] = name_exchange
                    bkex_data['price'] = price
                    bkex_data['symbol'] = sym + baseActive
                    if 'bkex' in mainExchange:
                        bkex_data['attrib'] = True
                        resultArray.append(bkex_data)
                    else:
                        bkex_data['attrib'] = False


            elif name_exchange == 'OKX' or name_exchange == 'KuCoin': #получение данных с Huobi или c KuCoin
                responses = requests.get(url + sym + '-' + baseActive).json()
                if name_exchange == 'OKX':
                    price = responses['data'][0]['idxPx']
                    okx_data['name'] = name_exchange
                    okx_data['price'] = price
                    okx_data['symbol'] = sym + baseActive
                    if 'okx' in mainExchange:
                        okx_data['attrib'] = True
                        resultArray.append(okx_data)
                    else:
                        okx_data['attrib'] = False


                elif name_exchange == 'KuCoin':
                    price = responses['data']['price']
                    kucoin_data['name'] = name_exchange
                    kucoin_data['price'] = price
                    kucoin_data['symbol'] = sym + baseActive
                    if 'kucoin' in mainExchange:
                        kucoin_data['attrib'] = True

                    else:
                        kucoin_data['attrib'] = False

            else: #получение данных с Binance или с Bybit
                responses = requests.get(url + sym + baseActive).json()
                if name_exchange == 'Binance':
                    price = responses['price']
                    binance_date['name'] = name_exchange
                    binance_date['price'] = price
                    binance_date['symbol'] = sym + baseActive
                    if 'binance' in mainExchange:
                        binance_date['attrib'] = True

                    else:
                        binance_date['attrib'] = False


                elif name_exchange == 'Bybit':
                    price = responses['result']['list'][0]['lastPrice']
                    bybit_date['name'] = name_exchange
                    bybit_date['price'] = price
                    bybit_date['symbol'] = sym + baseActive
                    if 'bybit' in mainExchange:
                        bybit_date['attrib'] = True

                    else:
                        bybit_date['attrib'] = False

                
    return resultArray


'''def test_get_data(): #метод для тестовых запросов
    url = 'https://api.bkex.com/v2/q/tickers?symbol=BTC_USDT'
    req = requests.get(url).json()
    print(req['data'][0]['close'])'''


l = ['Binance', 'Huobi', 'Bybit', 'OKX', 'KuCoin', 'BKEX'] #список бирж
print('Cписок бирж - ', l) 
mainExchange = input("Введи название биржи: ")
test = get_data(mainExchange, 'USDT', 100) #1 - главвная биржа, где храняться наши активы. 2 - базовый актив (пока будет USDT) 3 - кол-во монет (добавлю в будущем)
print("____")
print(test)