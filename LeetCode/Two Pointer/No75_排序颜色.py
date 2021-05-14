nums = [2, 0, 2, 1, 1, 0]


def sortColor(arr):
    x, y, z = 0, 0, 0  # 对应012

    for i in arr:
        if i == 0:
            arr[z] = 2
            z += 1
            arr[y] = 1
            y += 1
            arr[x] = 0
            x += 1
        elif i == 1:
            arr[z] = 2
            z += 1
            arr[y] = 1
            y += 1
        else:
            z += 1
        print(arr)
    return arr


print(sortColor(nums))
