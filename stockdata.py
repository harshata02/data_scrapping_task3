import requests as rq

import pandas as pd


stockdata=pd.read_csv('C:/Users/Welcome/Desktop/html-task/datascrapping/request/INR_stocks.csv',header=0)
print('stockdata',stockdata)

a1=stockdata.to_dict(orient='records')

for stock in stockdata.to_dict(orient='records'):

    print('stock',stock['currency'])

cUrl='https://api.coinbase.com/v2/exchange-rates'
cHeader={
    'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
} 
cParam={
    'currency':stock['currency']
}  
cResp=rq.get(url=cUrl,headers=cHeader,params=cParam) 


currencyData = cResp.json()
print(currencyData['data']['rates']['INR'])

stock['inr_rate'] =float(stock['price'])*float(currencyData['data']['rates']['INR'])
curr_df=pd.DataFrame(a1)
curr_df.to_csv('INR_Val.csv')

