import requests

# ====== 設定 ======
api_key = "CWA-65976294-2B02-4A3A-B429-66A72BD9252B"
webhook_url = "https://discord.com/api/webhooks/1495992362264952833/dzk-UUm4EE7KtCJ-PEIbwWPpz63OpFiE3B1Hn1YbbT7h5W5N3OE0ZWxinHcPj_0w7CVl"

# ====== 氣象API ======
url = f"https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-D0047-061?Authorization={api_key}&format=JSON"

data = requests.get(url).json()

# ====== 抓資料 ======
locations = data['records']['Locations'][0]['Location']
print(data)

for loc in locations:
    if loc['LocationName'] == "松山區":

        result = {}

        for e in loc['WeatherElement']:
            if e['ElementName'] == '溫度':
                
                result['T'] = e['Time'][0]['ElementValue'][0]['Temperature']
            elif e['ElementName'] == '體感溫度':
                result['AT'] = e['Time'][0]['ElementValue'][0]['ApparentTemperature']
            elif e['ElementName'] == '舒適度指數':
                result['CI'] = e['Time'][0]['ElementValue'][0]['ComfortIndexDescription']
            elif e['ElementName'] == '相對濕度':
                result['RH'] = e['Time'][0]['ElementValue'][0]['RelativeHumidity']

        # ====== 整理訊息 ======
        message = {
            "content": f""" 松山區天氣預報
溫度: {result['T']}°C
體感溫度: {result['AT']}°C
舒適度: {result['CI']}
濕度: {result['RH']}%
"""
        }

        # ====== 傳到 Discord ======
        requests.post(webhook_url, json=message)

        print("已傳送到 Discord")
        break