import requests

def lowercase_string(string):
    return string.lower()

binance_date = {}
bybit_date = {}
huobi_data = {}
bkex_data = {}
okx_data = {}
kucoin_data = {}
attrib = True

def get_data(mainExchange, baseActive, balance):
    list_crypto = ['BTC', 'ETH']
    return_list = []
    page_exchange = {
        'Binance': 'https://api.binance.com/api/v3/ticker/price?symbol=', 
        'Bybit': 'https://api.bybit.com/v5/market/tickers?category=inverse&symbol=', 
        'Huobi': 'https://api.huobi.pro/market/detail/merged?symbol=', 
        'OKX': 'https://aws.okx.com/api/v5/market/index-tickers?instId=',
        'KuCoin': 'http://api.kucoin.com/api/v1/market/orderbook/level1?symbol=', 
        'BKEX': 'https://api.bkex.com/v2/q/tickers?symbol=',
    }

    for sym in list_crypto:
        for name_exchange, url in page_exchange.items():
            if name_exchange == 'Huobi':
                responses = requests.get(url + lowercase_string(sym + baseActive)).json()
                huobi_data['name'] = name_exchange
                huobi_data['price'] = price
                huobi_data['symbol'] = sym + baseActive
                if mainExchange == 'Huobi':
                    huobi_data['attrib'] = True
                else:
                    huobi_data['attrib'] = False
                return_list.append(huobi_data)
                
            elif name_exchange == 'BKEX': 
                responses = requests.get(url + sym + '_' + baseActive).json()
                if name_exchange == 'BKEX':
                    price = responses['data'][0]['close']
                    bkex_data['name'] = name_exchange
                    bkex_data['price'] = price
                    bkex_data['symbol'] = sym + baseActive
                    if mainExchange == 'BKEX':
                        bkex_data['attrib'] = True
                    else:
                        bkex_data['attrib'] = False
                    return_list.append(bkex_data)
                    
            elif name_exchange == 'OKX' or name_exchange == 'KuCoin':
                responses = requests.get(url + sym + '-' + baseActive).json()
                if name_exchange == 'OKX':
                    price = responses['data'][0]['idxPx']
                    okx_data['name'] = name_exchange
                    okx_data['price'] = price
                    okx_data['symbol'] = sym + baseActive
                    if mainExchange == 'OKX':
                        okx_data['attrib'] = True
                    else:
                        okx_data['attrib'] = False
                    return_list.append(okx_data)
                    
                elif name_exchange == 'KuCoin':
                    price = responses['data']['price']
                    kucoin_data['name'] = name_exchange
                    kucoin_data['price'] = price
                    kucoin_data['symbol'] = sym + baseActive
                    if mainExchange == 'KuCoin':
                        kucoin_data['attrib'] = True
                    else:
                        kucoin_data['attrib'] = False
                    return_list.append(kucoin_data)
            else:
                responses = requests.get(url + sym + baseActive).json()
                if name_exchange == 'Binance':
                    price = responses['price']
                    binance_date['name'] = name_exchange
                    binance_date['price'] = price
                    binance_date['symbol'] = sym + baseActive
                    if mainExchange == 'Binance':
                        binance_date['attrib'] = True
                    else:
                        binance_date['attrib'] = False
                    return_list.append(binance_date)

                elif name_exchange == 'Bybit':
                    price = responses['result']['list'][0]['lastPrice']
                    bybit_date['name'] = name_exchange
                    bybit_date['price'] = price
                    bybit_date['symbol'] = sym + baseActive
                    if mainExchange == 'Bybit':
                        bybit_date['attrib'] = True
                    else:
                        bybit_date['attrib'] = False
                    return_list.append(bybit_date)
        
        return return_list

'''def test_get_data():
    url = 'https://api.bkex.com/v2/q/tickers?symbol=BTC_USDT'
    req = requests.get(url).json()
    print(req['data'][0]['close'])'''

l = ['Binance', 'Huobi', 'Bybit', 'OKX', 'KuCoin', 'BKEX']
print('Cписок бирж - ', l)
mainExchange = input("Введи название биржи: ")
print(get_data(mainExchange, 'USDT', 100))
