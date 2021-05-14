nums = [1, 8, 6, 2, 5, 4, 8, 3, 7]

#思路  对撞指针
def mostCuntWater(arr):
    max, start, stop = 0, 0, len(arr) - 1

    while start < stop:
        width = stop - start

        print(start,stop)
        if arr[start] > arr[stop]:
            hight = arr[stop]
            stop -= 1
        else:
            hight = arr[start]
            start += 1

        water = hight * width

        if water > max:
            max = water
        else:
            pass
    return (max)

print(mostCuntWater(nums))