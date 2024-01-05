import requests
import time
import json

while True:

    url = "https://api.upbit.com/v1/ticker?markets=KRW-BTC"
    
    headers = {"accept": "application/json"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)

    result = response.json()

    trade_price = result[0]['trade_price']  # 해당 코인의 현재가격

    print(f"현재가 : {trade_price:.0f}원")
    print(f"등락률 : {result[0]['signed_change_rate']}")
    print(f"최고가 : {result[0]['high_price']}")
    
    time.sleep(3)  # 3초 간격으로 요청

        


