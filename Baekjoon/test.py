array = [1, 2, 3, 4]

def test():
    global array
    array = [4, 5, 6, 7]
    array.append(3)
    print(array)
print(array)
test()
print(array)