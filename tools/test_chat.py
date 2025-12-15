import urllib.request, json

BASE = 'http://127.0.0.1:8000'

def get(path):
    url = BASE + path
    print('GET', url)
    try:
        r = urllib.request.urlopen(url, timeout=5)
        body = r.read().decode('utf-8')
        print('STATUS', r.status)
        print(body[:1000])
    except Exception as e:
        print('ERROR GET', e)


def post(path, data):
    url = BASE + path
    print('\nPOST', url, data)
    try:
        data_b = json.dumps(data).encode('utf-8')
        req = urllib.request.Request(url, data=data_b, headers={'Content-Type':'application/json'})
        r = urllib.request.urlopen(req, timeout=5)
        body = r.read().decode('utf-8')
        print('STATUS', r.status)
        print(body)
    except Exception as e:
        print('ERROR POST', e)


if __name__ == '__main__':
    get('/chat/')
    post('/chat/api/message/', {'message': '¿Cómo solicito vacaciones?'})
