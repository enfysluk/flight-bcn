import requests
from bs4 import BeautifulSoup
import json
import time

def get_direct_flights_from_bcn():
    # 爬取 BCN 直飞目的地的示例函数
    # 实际可用 kiwi.com 或其他API替代
    url = 'https://www.flightradar24.com/data/airports/bcn/routes'
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    flights = []
    for a in soup.select('table#tbl-routes tbody tr'):
        tds = a.find_all('td')
        if len(tds) >= 2:
            dest = tds[1].get_text(strip=True)
            flights.append(dest)
    return flights

def fetch_price_for_route(dest):
    # 模拟获取价格的函数（实际需接入航班价格API）
    # 这里返回随机价格示例
    import random
    return random.randint(50, 300)

def main():
    flights = get_direct_flights_from_bcn()
    data = []
    for dest in flights:
        price = fetch_price_for_route(dest)
        data.append({
            'destination': dest,
            'price': price
        })
        time.sleep(1)
    with open('data/flights.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print('Flight data saved to data/flights.json')

if __name__ == '__main__':
    main()
