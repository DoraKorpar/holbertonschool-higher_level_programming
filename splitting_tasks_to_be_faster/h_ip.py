import threading
import requests

class IPThread(threading.Thread):

    def __init__(self, ip, callback):
        threading.Thread.__init__(self)
        self.ip = ip
        self.callback = callback

    def run(self):
        print "Search: %s" % self.ip

        ip = "https://api.ip2country.info/ip?%s" % self.ip



        r = requests.get(ip)
        parsed = r.json()
        name = parsed['countryName']
        self.callback = name

        print "countryName: %s" % name
