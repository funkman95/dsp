import csv
import re
import string

name = []
degree = []
title = []
email = []

with open('/Users/samfunk/ds/metis/metisgh/prework/dsp/python/faculty.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        name.append(row[0])
        degree.append(row[1])
        title.append(row[2])
        email.append(row[3])

first_name = []
last_name = []
for n in name:
    first_name.append(n.split()[0])
    last_name.append(n.split()[-1])

#find different degrees
degs = []
for x, i in enumerate(degree):
    i = i.split()
    #degree[x] = i
    for y, j in enumerate(i):
        j = re.compile('[%s]' % re.escape(string.punctuation)).sub('', j)
        degs.append(j)
d = {x: degs.count(x) for x in degs}

#find different titles
tls = []
for i in title:
    prof = re.findall(r'(\w+)', i)[0]
    tls.append(prof.lower())
t = {x: tls.count(x) for x in tls}

#find different email domains
ems = []
for i in email:
    ems.append(re.search(r'@(.+)', i).group(1))
e = {x: ems.count(x) for x in ems}
