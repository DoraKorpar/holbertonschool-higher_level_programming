import urllib2
import json

request_headers = {
  'User-Agent': 'Holberton_School',
  'Authorization': 'token bc38982215eef8560352730fdfc6ee82bd22beee'
}

response = urllib2.urlopen('https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc')
html = response.read()

parsed_json = json.loads(html)

for i in range(len(parsed_json["items"])):
    print(parsed_json["items"][i]["full_name"])



