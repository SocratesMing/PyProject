import random

def dataList(n, low, high):
	m = []
	if low < high:
		for x in range(n):
			m.append(random.randint(low, high))
	else:
		print ('low >= high, 请重新输入')
	return m

def insertSort(data, n):
	x = 1
	while x < n:
		e = data[x]

		y = x
		while y >0 :
			if e < data[y-1]:
				data[y] = data[y-1]
			else:
				# data[y] = e
				break
			y -=1

		data[y] = e
		x += 1
		print (data)

if __name__ == '__main__':
	data = dataList(10, 0, 100)
	print (data)
	insertSort(data,len(data))