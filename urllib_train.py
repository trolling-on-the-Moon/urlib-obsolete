import urllib.request, urllib.parse, urllib.error
from urllib.request import Request
import re
import pprint

# Note: you may use file://, ftp:// instead of http as well
url = "https://docs.python.org"
url2 = "http://www.someserver.com/cgi-bin/register.cgi"
url3 = "http://localhost/website_forURLLIBtests/posted_form.php"

values3 = { 'nick' : 'SomeName',
            'pass' : 'SomePassword'}
data3 = urllib.parse.urlencode(values3)
full_url3 = url3 + '?' + data3
print(full_url3)

# There are 2 ways of constucting values, ths one and 2nd below:
# values = {'name' : 'Michael Foord',
#          'location' : 'Northampton',
#          'language' : 'Python' }
#
# or you may do with values like this:
# values2 = {}
# values2['name'] = 'Michael Foord'
# values2['location'] = 'Northampton'
# values2['language'] = 'Python'
# data2 = urllib.parse.urlencode(values2)
# print(data2) # so now data2 is 2nd part of url, like after http://... you see ? as GET, so just add data2 to url (url + '?' + data2)
# Note that other encodings are sometimes required (e.g. for file upload from HTML forms - see HTML Specification, Form Submission).
# data = urllib.parse.urlencode(values)

# for POST METHOD add extra parameter data made above:
req = urllib.request.Request(full_url3, data3)
# for GET METHOD pass only url:
req = urllib.request.Request(full_url3) # we could use only .urlopen() [for GET method] but .Request() [for POST method] allows me to also send extra data such as HEADERS. so if you do not pass the data argument, urllib will use a GET request.
response = urllib.request.urlopen(req)
html = response.read().decode() # add .decode() to decode from bytes; plain .read() shows html coded in bytes
print(html)
