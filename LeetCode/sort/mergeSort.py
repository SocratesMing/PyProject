import random

def dataList(n, low, high):
	m = []
	if low < high:
		for x in range(n):
			m.append(random.randint(low, high))
	else:
		print ('low >= high, 请重新输入')
	return m



def mergeSort(data, n):

	merge1(data, 0, n-1)

def merge1(data, l, r):

	if (l>=r):
		return

	mid = (l+r)/2

	merge1(data, l, mid)
	merge1(data, mid+1, r)

	merge2(data, l, mid, r)


 
def merge2(data, l, mid, r):
	aux = [0]*(l-r+1)

	i = l
	while i<=r:
		aux[i-l] = data[i]
		i += 1

	i = l
	j = mid+1
	k = l

	while k<= r :

		if i > mid:
			data[k] = aux[j-l]
			j += 1

		elif j > r: 
			data[k] = aux[i-l]
			i += 1

		elif (aux[i-l] < aux[j-l]):
			data[k] = aux[i-l]
			i += 1

		elif (aux[i-l] > aux[j-l]):
			data[k] = aux[j-l]
			j += 1

		k += 1





if __name__ == '__main__':
	data = dataList(2, 0, 100)
	print (data)
	mergeSort(data,len(data))