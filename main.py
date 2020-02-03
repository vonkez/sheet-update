#!/usr/bin/python3.6
import price
import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds']
name = 'arb'

credentials = ServiceAccountCredentials.from_json_keyfile_name('cred.json', scope)

gc = gspread.authorize(credentials)

while True:
    wks = gc.open(name).sheet1
    wks.update_acell('I2', price.enpara()[1])
    wks.update_acell('I5', price.bigpara()[1])

    wks.update_acell('B2', price.lykke()[2])
    wks.update_acell('B3', price.lykke()[0])
    wks.update_acell('A1', time.strftime('%H:%M:%S', time.localtime()))
    print('lykke updated')

    wks.update_acell('C2', price.koineks()[3])
    wks.update_acell('C3', price.koineks()[1])
    wks.update_acell('A1', time.strftime('%H:%M:%S', time.localtime()))
    print('koineks updated')

    wks.update_acell('E3', price.paribu()[1])
    wks.update_acell('A1', time.strftime('%H:%M:%S', time.localtime()))
    print('paribu updated')

    wks.update_acell('G2', price.btcturk()[3])
    wks.update_acell('G3', price.btcturk()[1])
    wks.update_acell('A1', time.strftime('%H:%M:%S', time.localtime()))
    print('btcturk updated')

    print('--------------------')
    time.sleep(60)

