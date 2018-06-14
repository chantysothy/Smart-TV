import requests
import json
import csv

headers = {
    'User-Agent': 'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52'
}

data = [
    ['name', 'cn', 'attach'],
]

response = requests.get('http://api.ndasat.com/bbb.php?login=1111111111111111&uid=8902167307'
                        '&model=tiger', headers=headers)

dict_data = json.loads(response.text)
for attach in dict_data['packages']:
    response = requests.get('http://api.ndasat.com/ccc.php?login=1111111111111111&pack_id='
                            '%s&uid=8902167307&model=tiger' % attach['id'], headers=headers)
    info_data = json.loads(response.text)
    for info in info_data['chanels']:
        info_list = [info['name'], info['ch'], attach['name']]
        data.append(info_list)


with open('example.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(data)

# 47个国家
