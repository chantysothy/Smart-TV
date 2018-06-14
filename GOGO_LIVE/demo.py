import requests
import json

headers = {
    'User-Agent': 'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52'
}

data = [
    ['name', 'ts', 'attach'],
]

l = set()

country_list = []

response = requests.get('http://api.oneiptv.tv/iptv/serv7.php?'
                        'code=227843730628346&uid=8902167307&serial=7902167307&model=icone', headers=headers)

dict_data = json.loads(response.text)
for attach in dict_data['packages']:
    for info in dict_data['packages'][attach]:
        l.add(attach)

print(l)
print(len(l))
# 38个国家

