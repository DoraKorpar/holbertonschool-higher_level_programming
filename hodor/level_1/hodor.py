import requests

url = 'http://173.246.108.142/level1.php'
i = 0
while i < 1024:
    data = ({'id': '28', 'holdthedoor': 'Submit', 'key': ''})
    headers = {'Cookie': 'HoldTheDoor='}

    r = requests.post(url, data, headers=headers)

    print ("Voted %d times" % (i + 1))
    i += 1
