#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import csv
import sys
import urllib2
import re
import math
import operator

parser = argparse.ArgumentParser(description="url where the file is located")
parser.add_argument('url',type=str,help='URL of the file')
args = parser.parse_args()

req = urllib2.Request(args.url)
response = urllib2.urlopen(req)
    
"""searches for all hits that are for an image file and most popular browser"""
reader = csv.reader(response)
Counter_total_lines=0
Counter_images=0
Counter=0
Counter_Firefox=0
Counter_Chrome=0
Counter_Explorer=0
Counter_Safari=0
for row in reader:
    Counter+=1
    Counter_total_lines+=1
    if re.search('.gif',row[0],re.IGNORECASE): Counter_images+=1
    if re.search('.jpg',row[0],re.IGNORECASE): Counter_images+=1
    if re.search('.png',row[0],re.IGNORECASE): Counter_images+=1
    if re.search('Firefox',row[2],re.IGNORECASE): Counter_Firefox+=1
    if re.search('Safari',row[2],re.IGNORECASE):
        if re.search('Chrome',row[2],re.IGNORECASE)== None:
            Counter_Safari+=1
            print row[2]
    if re.search('Chrome',row[2],re.IGNORECASE): Counter_Chrome+=1         
    if re.search('Explorer',row[2],re.IGNORECASE): Counter_Explorer+=1
     

Percentage_images = round(Counter_images * 100) / Counter_total_lines
print 'Image requests account for ' + str(Percentage_images) + ' percent of all requests'


Browsers={'Safari':Counter_Safari, 'Firefox':Counter_Firefox, 'Explorer':Counter_Explorer,'Chrome':Counter_Chrome}
print max(Browsers.iteritems(), key=operator.itemgetter(1))[0]



