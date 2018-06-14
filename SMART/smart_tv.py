import csv
import requests
import json

data = [
    ['name', 'ch', 'logo', 'attach'],
]

headers = {
    'User-Agent': 'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52'
}

arabic_list = [
    'http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=10&uid=8902167307&serial=7902167307&model=stb-model',
    'http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=15&uid=8902167307&serial=7902167307&model=stb-model',
    'http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=20&uid=8902167307&serial=7902167307&model=stb-model',
    'http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=24&uid=8902167307&serial=7902167307&model=stb-model',
    'http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=47&uid=8902167307&serial=7902167307&model=stb-model',
    'http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=14&uid=8902167307&serial=7902167307&model=stb-model',
    'http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=13&uid=8902167307&serial=7902167307&model=stb-model',
    'http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=39&uid=8902167307&serial=7902167307&model=stb-model',
    'http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=18&uid=8902167307&serial=7902167307&model=stb-model',
    'http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=19&uid=8902167307&serial=7902167307&model=stb-model',
    'http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=21&uid=8902167307&serial=7902167307&model=stb-model',
    'http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=16&uid=8902167307&serial=7902167307&model=stb-model',
    'http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=17&uid=8902167307&serial=7902167307&model=stb-model',
    'http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=41&uid=8902167307&serial=7902167307&model=stb-model',
    'http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=40&uid=8902167307&serial=7902167307&model=stb-model',
]

canal_list = [
    'http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=29&uid=8902167307&serial=7902167307&model=stb-model',
    'http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=12&uid=8902167307&serial=7902167307&model=stb-model',
    'http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=35&uid=8902167307&serial=7902167307&model=stb-model',
]

sky_list = [
    'http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=22&uid=8902167307&serial=7902167307&model=stb-model',
    'http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=25&uid=8902167307&serial=7902167307&model=stb-model',
    'http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=31&uid=8902167307&serial=7902167307&model=stb-model',
]

other_list = [
    'http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=37&uid=8902167307&serial=7902167307&model=stb-model',
    'http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=33&uid=8902167307&serial=7902167307&model=stb-model',
    'http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=48&uid=8902167307&serial=7902167307&model=stb-model',
    'http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=44&uid=8902167307&serial=7902167307&model=stb-model',
    'http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=43&uid=8902167307&serial=7902167307&model=stb-model',
    'http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=23&uid=8902167307&serial=7902167307&model=stb-model',
    'http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=26&uid=8902167307&serial=7902167307&model=stb-model',
    'http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=34&uid=8902167307&serial=7902167307&model=stb-model',
    'http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=45&uid=8902167307&serial=7902167307&model=stb-model',
    'http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=46&uid=8902167307&serial=7902167307&model=stb-model',
    'http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=42&uid=8902167307&serial=7902167307&model=stb-model',
    'http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=49&uid=8902167307&serial=7902167307&model=stb-model',
    'http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=50&uid=8902167307&serial=7902167307&model=stb-model',
]

box_list = [
    'http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=32&uid=8902167307&serial=7902167307&model=stb-model',
    'http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=27&uid=8902167307&serial=7902167307&model=stb-model',
    'http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=30&uid=8902167307&serial=7902167307&model=stb-model',
]


def h265(attach):
    response = requests.get('http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=0'
                            '&uid=8902167307&serial=7902167307&model=stb-model', headers=headers)
    dict_data = json.loads(response.text)
    for h in dict_data['channels']:
        h265_list = [h['name'], h['ch'], h['logo'], attach]
        data.append(h265_list)


def bein_sports(attach):
    response = requests.get('http://amigo4.ddnb.tn/channels.php?login=104311061936337&pack_id=1'
                            '&uid=8902167307&serial=7902167307&model=stb-model', headers=headers)
    dict_data = json.loads(response.text)
    for h in dict_data['channels']:
        h265_list = [h['name'], h['ch'], h['logo'], attach]
        data.append(h265_list)


def arabic_channels(attach):
    response = requests.get('http://amigo4.ddnb.tn/pack.php?login=104311061936337'
                            '&pack_id=2&uid=8902167307&serial=7902167307&model=stb-model', headers=headers)
    dict_data = json.loads(response.text)
    for url, channel_name in zip(arabic_list, dict_data['bouquets']):
        response = requests.get(url, headers=headers)
        dict_data = json.loads(response.text)
        for h in dict_data['channels']:
            h265_list = [h['name'], h['ch'], h['logo'], attach + '>' + channel_name['name']]
            data.append(h265_list)


def canal(attach):
    response = requests.get('http://amigo4.ddnb.tn/pack.php?login=104311061936337&pack_id=3'
                            '&uid=8902167307&serial=7902167307&model=stb-model', headers=headers)
    dict_data = json.loads(response.text)
    for url, channel_name in zip(canal_list, dict_data['bouquets']):
        response = requests.get(url, headers=headers)
        dict_data = json.loads(response.text)
        for h in dict_data['channels']:
            h265_list = [h['name'], h['ch'], h['logo'], attach + '>' + channel_name['name']]
            data.append(h265_list)


def sky(attach):
    response = requests.get('http://amigo4.ddnb.tn/pack.php?login=104311061936337'
                            '&pack_id=4&uid=8902167307&serial=7902167307&model=stb-model', headers=headers)
    dict_data = json.loads(response.text)
    for url, channel_name in zip(sky_list, dict_data['bouquets']):
        response = requests.get(url, headers=headers)
        dict_data = json.loads(response.text)
        for h in dict_data['channels']:
            h265_list = [h['name'], h['ch'], h['logo'], attach + '>' + channel_name['name']]
            data.append(h265_list)


def other_packages(attach):
    response = requests.get('http://amigo4.ddnb.tn/pack.php?login=104311061936337&pack_id=5'
                            '&uid=8902167307&serial=7902167307&model=stb-model', headers=headers)
    dict_data = json.loads(response.text)
    for url, channel_name in zip(other_list, dict_data['bouquets']):
        response = requests.get(url, headers=headers)
        dict_data = json.loads(response.text)
        for h in dict_data['channels']:
            h265_list = [h['name'], h['ch'], h['logo'], attach + '>' + channel_name['name']]
            data.append(h265_list)


def box_office(attach):
    response = requests.get('http://amigo4.ddnb.tn/pack.php?login=104311061936337&pack_id=6'
                            '&uid=8902167307&serial=7902167307&model=stb-model', headers=headers)
    dict_data = json.loads(response.text)
    for url, channel_name in zip(other_list, dict_data['bouquets']):
        response = requests.get(url, headers=headers)
        dict_data = json.loads(response.text)
        for h in dict_data['channels']:
            h265_list = [h['name'], h['ch'], h['logo'], attach + '>' + channel_name['name']]
            data.append(h265_list)


def channel_list():
    response = requests.get('http://amigo4.ddnb.tn/pack.php?login=104311061936337&uid=8902167307'
                            '&serial=7902167307&model=stb-model', headers=headers)
    dict_data = json.loads(response.text)
    for h in dict_data['bouquets']:
        if h['name'] == 'H265':
            h265(h['name'])
        if h['name'] == 'Bein Sports':
            bein_sports(h['name'])
        if h['name'] == 'Arabic Channels':
            arabic_channels(h['name'])
        if h['name'] == 'Canal +':
            canal(h['name'])
        if h['name'] == 'SKY':
            sky(h['name'])
        if h['name'] == 'Other Packages':
            other_packages(h['name'])
        if h['name'] == 'Box Office':
            box_office(h['name'])


channel_list()

with open('example.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(data)
