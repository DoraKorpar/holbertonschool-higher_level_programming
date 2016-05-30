import requests

url = "http://173.246.108.142/level0.php"
data = ({'id': '28', 'holdthedoor': 'SUBMIT'})

i = 0
while i < 1024:
    r = requests.post(url, data)
    print ("Voted %d times" % (i + 1))
    i += 1
