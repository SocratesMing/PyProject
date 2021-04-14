import random

def dataList(n, low, high):
	m = []
	if low < high:
		for x in range(n):
			m.append(random.randint(low, high))
	else:
		print ('low >= high, 请重新输入')
	return m

def bubbleSort(data, n):
	x = 0
	
	while x < n:
		print (x)
		y = 0
		while  y < n-1:
			if data[y] > data[y+1]:
				data[y], data[y+1] = data[y+1], data[y]
			else:
				pass

			y += 1

		x += 1

		print (data)


	print (data)

if __name__ == '__main__':
	data = dataList(10, 0, 100)
	print (data)
	bubbleSort(data,len(data))