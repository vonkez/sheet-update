from splinter import Browser
import requests


browser = Browser('phantomjs')


def bigpara():
    browser.visit('http://bigpara.hurriyet.com.tr/doviz/dolar-ne-kadar')

    buyUsd = browser.evaluate_script('document.getElementsByClassName("result")[0].innerHTML')
    sellUsd = buyUsd

    return [buyUsd, sellUsd]


def enpara():
    browser.visit('https://www.qnbfinansbank.enpara.com/doviz-kur-bilgileri/doviz-altin-kurlari.aspx')

    buyUsd = browser.evaluate_script('document.getElementsByClassName("dlCont")[1].childNodes[0].innerHTML')[:-4]
    sellUsd = browser.evaluate_script('document.getElementsByClassName("dlCont")[2].childNodes[0].innerHTML')[:-4]

    return [buyUsd, sellUsd]


def isbank():
    browser.visit('https://www.isbank.com.tr/TR/fiyatlar-ve-oranlar/doviz-kurlari/Sayfalar/doviz-kurlari.aspx')

    buyUsd = browser.evaluate_script('document.getElementsByClassName("dK_Line_Item2")[0].innerHTML')
    sellUsd = browser.evaluate_script('document.getElementsByClassName("dK_Line_Item3")[0].innerHTML')

    return [buyUsd, sellUsd]


def btcturk():
    url = 'https://www.btcturk.com/api/ticker'

    response = requests.request("GET", url)
    r = response.json()

    btcBuy = str(r[0]['ask']).replace('.', ',')
    btcSell = str(r[0]['bid']).replace('.', ',')

    ethBuy = str(r[2]['ask']).replace('.', ',')
    ethSell = str(r[2]['bid']).replace('.', ',')

    return [btcBuy, btcSell, ethBuy, ethSell]


def bitfinex():
    btcUrl = "https://api.bitfinex.com/v1/pubticker/btcusd"
    ethUrl = "https://api.bitfinex.com/v1/pubticker/ethusd"

    response = requests.request("GET", btcUrl)
    r = response.json()
    btcBuy = r['last_price'].replace('.', ',')

    btcSell = btcBuy

    response = requests.request("GET", ethUrl)
    r = response.json()
    ethBuy = r['last_price'].replace('.', ',')
    ethSell = ethBuy

    return [btcBuy, btcSell, ethBuy, ethSell]


def lykke():
    btcUrl = "https://lykke-public-api.azurewebsites.net/api/AssetPairs/rate/BTCUSD"
    ethUrl = "https://lykke-public-api.azurewebsites.net/api/AssetPairs/rate/ETHUSD"
    response = requests.request("GET", btcUrl)
    # print('lykke btc response:', response.text)
    while not response.text.startswith('{'):
        response = requests.request("GET", btcUrl)
        print(response.text, 'retrying btc')
    r = response.json()

    btcBuy = str(r['ask']).replace('.', ',')
    btcSell = str(r['bid']).replace('.', ',')

    response = requests.request("GET", ethUrl)
    # print('lykke eth response:', response.text)
    while not response.text.startswith('{'):
        response = requests.request("GET", ethUrl)
        print('lykke invalid response, retrying', response.text)

    r = response.json()

    ethBuy = str(r['ask']).replace('.', ',')
    ethSell = str(r['bid']).replace('.', ',')

    return [btcBuy, btcSell, ethBuy, ethSell]


def paribu():
    browser.visit('https://www.btcmerkezi.com/paribu/')

    btcBuy = browser.evaluate_script('document.getElementsByClassName("text-right")[7].innerHTML')[:-6].replace(',', '')
    btcSell = btcBuy

    return [btcBuy, btcSell]


def koinim():
    browser.visit('https://koinim.com/')

    btcBuy = browser.evaluate_script('document.getElementsByClassName("nav-BTC-price")[0].innerHTML').replace('.', ',')
    btcSell = btcBuy

    return [btcBuy, btcSell]


def koineks():
    url = "https://koineks.com/ticker"

    response = requests.request("GET", url)
    r = response.json()

    btcBuy = r['BTC']['ask'].replace('.', ',')
    btcSell = r['BTC']['bid'].replace('.', ',')

    ethBuy = r['ETH']['ask'].replace('.', ',')
    ethSell = r['ETH']['bid'].replace('.', ',')

    return [btcBuy, btcSell, ethBuy, ethSell]
