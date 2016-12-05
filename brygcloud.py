#!/usr/bin/python
import urllib
import urllib2

# For now, we use ThingSpeak for our data needs
def push(payload, endpoint):
    try:
        data = urllib.urlencode(payload)
        req = urllib2.Request(endpoint, data)
        return urllib2.urlopen(req)
    except urllib2.HTTPError as e:
        print "No interwebs / endpoint down? =>", e