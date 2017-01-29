#!/usr/bin/python

import sys
import os

array = []
list = []
sum = 0.0
virtual = 2000.0
cnt = 0
factor = 1024.0/virtual

for line in sys.stdin:
	list = line.split(":")
	list[3] = int(list[3])
	sum += list[3]
	if list[3] == 50:
		cnt += 1
	array.append(list)

if sum <= virtual:
	os.system('echo score:1.0')
	#print "score:%f" % (1.0)
else:
	os.system('echo score:-1.0')
	#print "score:%f" % (-1.0)

for i in array:
	if virtual-sum > 0:
		if i[3] == 50:
			i[3] = i[3]+(virtual-sum)/cnt
		elif cnt == 0:
			i[3] = i[3]+(virtual-sum)*(float(i[3]))/sum
        	i[3] = i[3]*factor
		os.system('echo '+'set_limit:'+i[1]+':cpu.shares:'+str(int(i[3])))
	else:
		i[3] = i[3]*factor
		os.system('echo '+'set_limit:'+i[1]+':cpu.shares:'+str(int(i[3])))

