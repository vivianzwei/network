# -*- coding:utf-8 -*- 
import sys
import numpy as np
# sys.path.append('/Users/vivian/Documents/Projects/libpython')
sys.path.append('lib')

import network_csv

table = network_csv.read('data.csv')


head = table['head']
col = table['col']
data = table['data']

cols = 3
rows = len(col)*len(head) + 1
# result = [[0 for col in range(cols)] for row in range(rows)]
result = []

# result[0][0] = 'from'
# result[0][1] = 'to'
# result[0][2] = 'weight'
result.append(['from','to','weight'])

for i,h in enumerate(head):
	for j,c in enumerate(col):
		if h != c:
			result.append([head[i],col[j],data[j][i]])
		# result[i*len(col) + j + 1][0] = head[i]
		# result[i*len(col) + j + 1][1] = col[j]
		# result[i*len(col) + j + 1][2] = data[j][i]
network_csv.list2csv(result,'edge.csv')








