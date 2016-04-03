import urllib2

request_headers = {
  'User-Agent': 'Holberton_School',
  'Authorization': 'token bc38982215eef8560352730fdfc6ee82bd22beee'
}

response = urllib2.urlopen('https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc')
html = response.read()

target = open("/tmp/28", "w")
target.truncate()
target.write(html)
print "The file was saved!"
target.close()

