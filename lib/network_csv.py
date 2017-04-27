# -*- coding:utf-8 -*- 
import io

def read(file):
	result = {
		'head':[],
		'col':[],
		'data':[],
		'matrix':[]
	}

	with io.open(file, 'r', encoding='UTF-8') as f:
		flag = True
		for line in f:
			ld = line.replace('\n','').split(',')
			result['matrix'].append(ld)

			if flag == True:
				result['head'] = ld[1:]
			else:
				result['col'].append(ld[0])
				result['data'].append(ld[1:])
			flag = False
	return result

def list2csv(list,file):
	str1=','
	str2='\n'
	with io.open(file, 'x', encoding='UTF-8') as f:
		for line in list:
			f.write(str1.join(line) + str2)

if __name__ == '__main__':
	print(network_csv_read('./Desktop/data.csv'))

