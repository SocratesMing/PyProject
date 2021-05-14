count = []

def test(count):

    for x in range(9):
        count.append(x)

    test2(count)
    cout = count[:3]


def test2(count):
    for x in range(9,20):
        count.append(x)
test(count)
print(count)


