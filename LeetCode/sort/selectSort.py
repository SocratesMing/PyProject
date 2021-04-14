import random

def dataList(n, low, high):
	m = []
	if low < high:
		for x in range(n):
			m.append(random.randint(low, high))
	else:
		print ('low >= high, 请重新输入')
	return m

def selectSort(data, n):
	z = 0
	for x in range(n):
		minIndex = x		
		for y in range(n-1-z):
			if data[y+1+z] <= data[minIndex]:
				minIndex = y+1+z
			else:
				pass
		data[minIndex], data[x] = data[x], data[minIndex]

		z += 1
		print (data)

if __name__ == '__main__':
	data = dataList(10, 0, 100)
	print (data)

	selectSort(data,len(data))




# print (x)