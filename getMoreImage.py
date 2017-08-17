# -*- coding: utf-8 -*-
import re
import urllib
import os

def getHtmlFor(url):
	res = urllib.urlopen(url)
	html = res.read()
	return html

def getImageUrl(html):
	r = r'src="(.*\.jpg)'
	reImage = re.compile(r)
	imageList = re.findall(reImage, html)
	return imageList;

def saveImage(imageList):
	path = "imageSource"
	isPath = os.path.exists(path)
	if not isPath:
		os.makedirs(path)

	i = 0;
	for url in imageList:
		# u = urllib.urlopen(url)
		# name = path + "/" + "%s.jpg" %i
		# data = u.read()
		# f = open(name, 'wb')
		# f.write(data)
		# f.close()


		urllib.urlretrieve(url, path + "/" + '%s.jpg' %i)
		i += 1

html = getHtmlFor('http://www.nipic.com/index.html')

imageList = getImageUrl(html)

saveImage(imageList)

