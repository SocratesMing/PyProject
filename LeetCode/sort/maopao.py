import random

def dataList(n, low, high):
	m = []
	if low < high:
		for x in range(n):
			m.append(random.randint(low, high))
	else:
		print ('low >= high, 请重新输入')
	return m

def sortBubble(data):



if __name__ == '__main__':
	data = dataList(20, 0, 100)


print (x)