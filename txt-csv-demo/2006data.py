import io
def list2csv(list,file):
	str1=','
	str2='\n'
	with io.open(file, 'x', encoding='UTF-8') as f:
		for line in list:
			f.write(str1.join(line) + str2)

data = []
f = open('2006.txt','r')

try:
	while 1:
		i = 0
		a = []
		while i < 6:
			i = i + 1
			line = next(f)
			if not line:
				break
				pass
			a = a + line.split( )
		data.append(a)
	pass
except StopIteration:
    print('here is end')

for i in range(len(data)):
	data[i][0] = data[i][0][0:-6]
	data[i].insert(1,'-180.0')

list2csv(data,'2006.csv')
f.close

