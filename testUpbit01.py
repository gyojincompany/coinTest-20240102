import requests
import time
import json

while True:

    url = "https://api.upbit.com/v1/ticker?markets=KRW-XRP"
    
    headers = {"accept": "application/json"}
    
    response = requests.get(url, headers=headers)
    
    # print(response.text)

    result = response.json()

    trade_price = result[0]['trade_price']  # 해당 코인의 현재가격
    acc_trade_volume_24h = result[0]['acc_trade_volume_24h']  # 24시간 누적 거래량
    acc_trade_price_24h = result[0]['acc_trade_price_24h']  # 24시간 누적 거래대금
    trade_volume = result[0]['trade_volume']  # 가장 최근 거래량
    high_price = result[0]['high_price']  # 고가
    low_price = result[0]['low_price']  # 저가
    prev_closing_price = result[0]['prev_closing_price']  # 전일 종가
    signed_change_rate = result[0]['signed_change_rate']  # 부호가 있는 변화율

    # print(f"현재가 : {trade_price:.0f}원")
    # print(f"등락률 : {result[0]['signed_change_rate']}")
    # print(f"최고가 : {result[0]['high_price']}")
    print(trade_price)
    print(acc_trade_volume_24h)
    print(acc_trade_price_24h)
    print(trade_volume)
    print(high_price)
    print(low_price)
    print(prev_closing_price)
    print(signed_change_rate)

    print('----------------------------------------')

    time.sleep(3)  # 3초 간격으로 요청

        


