import urllib3
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

http = urllib3.PoolManager()
r = http.request('GET', 'http://py4e-data.dr-chuck.net/comments_728999.xml')
tree = ET.fromstring(r.data)
counts = tree.findall('.//count')

x = 0
for count in counts:
    x = x + int(count.text)

print(x)