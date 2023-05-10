import requests

def lowercase_string(string):
    return string.lower()

binance_data = {}
bybit_data = {}
huobi_data = {}
bkex_data = {}
okx_data = {}
kucoin_data = {}
bitget_data = {}
gate_data = {}
mexc_data = {}
kraken_data = {}
bitfinex_data = {}
cryptoCom_data = {}

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
        'BitGet': 'https://api.bitget.com/api/spot/v1/market/ticker?symbol=', 
        'Gate': 'https://api.gateio.ws/api/v4/spot/tickers?currency_pair=', 
        'MEXC': 'https://api.mexc.com/api/v3/ticker/price?symbol=',
        'Kraken': 'https://api.kraken.com/0/public/Ticker?pair=', 
        'Bitfinex': 'https://api-pub.bitfinex.com/v2/ticker/t', 
        'Crypto.com': 'https://api.crypto.com/exchange/v1/public/get-tickers?instrument_name=', 
    }
    for sym in list_crypto:
        for name_exchange, url in page_exchange.items():
            if name_exchange == 'Huobi':
                responses = requests.get(url + lowercase_string(sym + baseActive)).json()
                try:
                    huobi_data['name'] = name_exchange
                    huobi_data['price'] = price
                    huobi_data['symbol'] = sym + baseActive
                    if mainExchange == 'Huobi':
                        huobi_data['main'] = True
                    else:
                        huobi_data['main'] = False
                    return_list.append(huobi_data)
                except:
                    print(f'Not pair - {name_exchange}')
                
            elif name_exchange == 'BKEX' or name_exchange == 'Gate': 
                responses = requests.get(url + sym + '_' + baseActive).json()
                if name_exchange == 'BKEX':
                    try:
                        price = responses['data'][0]['close']
                        bkex_data['name'] = name_exchange
                        bkex_data['price'] = price
                        bkex_data['symbol'] = sym + baseActive
                        if mainExchange == 'BKEX':
                            bkex_data['main'] = True
                        else:
                            bkex_data['main'] = False
                        return_list.append(bkex_data)
                    except:
                        print(f'Not pair - {name_exchange}')
                        
                elif name_exchange == 'Gate':
                    try:
                        price = responses[0]['last']
                        gate_data['name'] = name_exchange
                        gate_data['price'] = price
                        gate_data['symbol'] = sym + baseActive
                        if mainExchange == 'Gate':
                            gate_data['main'] = True
                        else:
                            gate_data['main'] = False
                        return_list.append(gate_data)
                    except:
                        print(f'Not pair - {name_exchange}')

            elif name_exchange == 'BitGet':
                responses = requests.get(url + sym + baseActive + '_SPBL').json()
                try:
                    price = responses['data']['close']
                    bitget_data['name'] = name_exchange
                    bitget_data['price'] = price
                    bitget_data['symbol'] = sym + baseActive  
                    if mainExchange == 'BitGet':
                        bitget_data['main'] = True
                    else:
                        bitget_data['main'] = False
                    return_list.append(bitget_data)
                except:
                        print(f'Not pair - {name_exchange}')

            elif name_exchange == 'Crypto.com':
                responses = requests.get(url + sym + baseActive + '-PERP').json()
                try:    
                    price = responses['result']['data'][0]['a']
                    cryptoCom_data['name'] = name_exchange
                    cryptoCom_data['price'] = price
                    cryptoCom_data['symbol'] = sym + baseActive  
                    if mainExchange == 'Crypto.com':
                        cryptoCom_data['main'] = True
                    else:
                        cryptoCom_data['main'] = False
                    return_list.append(cryptoCom_data)
                except:
                        print(f'Not pair - {name_exchange}')

            elif name_exchange == 'OKX' or name_exchange == 'KuCoin':
                responses = requests.get(url + sym + '-' + baseActive).json()
                if name_exchange == 'OKX':
                    try:
                        price = responses['data'][0]['idxPx']
                        okx_data['name'] = name_exchange
                        okx_data['price'] = price
                        okx_data['symbol'] = sym + baseActive
                        if mainExchange == 'OKX':
                            okx_data['main'] = True
                        else:
                            okx_data['main'] = False
                        return_list.append(okx_data)
                    except:
                        print(f'Not pair - {name_exchange}')

                elif name_exchange == 'KuCoin':
                    try:
                        price = responses['data']['price']
                        kucoin_data['name'] = name_exchange
                        kucoin_data['price'] = price
                        kucoin_data['symbol'] = sym + baseActive
                        if mainExchange == 'KuCoin':
                            kucoin_data['main'] = True
                        else:
                            kucoin_data['main'] = False
                        return_list.append(kucoin_data)
                    except:
                        print(f'Not pair - {name_exchange}')

            else:
                responses = requests.get(url + sym + baseActive).json()
                if name_exchange == 'Binance':
                    try:
                        price = responses['price']
                        binance_data['name'] = name_exchange
                        binance_data['price'] = price
                        binance_data['symbol'] = sym + baseActive
                        if mainExchange == 'Binance':
                            binance_data['main'] = True
                        else:
                            binance_data['main'] = False
                        return_list.append(binance_data)
                    except:
                        print(f'Not pair - {name_exchange}')

                elif name_exchange == 'Bybit':
                    try:
                        price = responses['result']['list'][0]['lastPrice']
                        bybit_data['name'] = name_exchange
                        bybit_data['price'] = price
                        bybit_data['symbol'] = sym + baseActive
                        if mainExchange == 'Bybit':
                            bybit_data['main'] = True
                        else:
                            bybit_data['main'] = False
                        return_list.append(bybit_data)
                    except:
                        print(f'Not pair - {name_exchange}')

                elif name_exchange == 'MEXC':
                    try:
                        price = responses['price']
                        mexc_data['name'] = name_exchange
                        mexc_data['price'] = price
                        mexc_data['symbol'] = sym + baseActive
                        if mainExchange == 'MEXC':
                            mexc_data['main'] = True
                        else:
                            mexc_data['main'] = False
                        return_list.append(mexc_data)
                    except:
                        print(f'Not pair - {name_exchange}')

                elif name_exchange == 'Kraken':
                    try:
                        s = list(responses['result'].keys())
                        price = responses['result'][s[0]]['c'][0]
                        kraken_data['name'] = name_exchange
                        kraken_data['price'] = price
                        kraken_data['symbol'] = sym + baseActive
                        if mainExchange == 'Kraken':
                            kraken_data['main'] = True
                        else:
                            kraken_data['main'] = False
                        return_list.append(kraken_data)
                    except:
                        print(f'Not pair - {name_exchange}')

                elif name_exchange == 'Bitfinex':
                    try:
                        price = responses[6]
                        bitfinex_data['name'] = name_exchange
                        bitfinex_data['price'] = price
                        bitfinex_data['symbol'] = sym + baseActive
                        if mainExchange == 'Bitfinex':
                            bitfinex_data['main'] = True
                        else:
                            bitfinex_data['main'] = False
                        return_list.append(bitfinex_data)
                    except:
                        print(f'Not pair - {name_exchange}')

        return return_list
                

def test_get_data():
    url = 'https://api.crypto.com/exchange/v1/public/get-tickers?instrument_name=BTCUSD-PERP'
    req = requests.get(url).json()
    print(req['result']['data'][0]['a'])

#test_get_data()

'''l = ['Binance', 'Huobi', 'Bybit', 'OKX', 'KuCoin', 'BKEX', 'Gate', 'BitGet', ]
print('Cписок бирж - ', l)
mainExchange = input("Введи название биржи: ")
print(get_data(mainExchange, 'EUR', 100))'''
