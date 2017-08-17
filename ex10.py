import urllib
import re
import os

response = urllib.urlopen("http://tieba.baidu.com/p/2211929933#!/l/p1")

hContent = response.read()

print (hContent)

urllist = re.findall(r'src="(.*?\.png)"', hContent, re.I)

filepath = os.getcwd()+'/pythoImage'
if os.path.exists(filepath) is False:
	os.mkdir(filepath)

x = 0
for i in urllist:
	temp = filepath + '/%s.jpg' % x
	urllib.urlretrieve(i, temp)
	x += 1

print(urllist)