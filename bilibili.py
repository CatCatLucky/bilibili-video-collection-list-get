import requests
import json
import bv2av
bv = input('请输入BV号:')
av = bv2av.bv_to_av(bv)
print(av)
url = 'https://api.bilibili.com/x/player/pagelist?aid='+av+'&jsonp=jsonp'

response = requests.get(url=url)
data_dict = json.loads(response.text)

for item in data_dict['data']:
    # print(item['page'],item['part'])
    print(item['part'])