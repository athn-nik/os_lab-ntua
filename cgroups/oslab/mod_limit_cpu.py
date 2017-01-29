#!/usr/bin/python

import sys
import os

list = []
for line in sys.stdin:
	list = line.split(":")
	list[3] = list[3].split('\n')
	path = '/sys/fs/cgroup/cpu/'+list[1]+'/'+list[3][0]
	if (list[0] == "create"):
		os.system("mkdir -p "+path)
	elif (list[0] == "remove"):
		os.system("rmdir "+path)
	elif (list[0] == "add"):
		path += '/tasks'
		list[4] = list[4].split('\n')
		os.system('echo '+list[4][0]+' >> '+path)
	else:
		path += '/cpu.shares'
		list[5] = list[5].split('\n')
		os.system('echo '+list[5][0]+' > '+path)
