def binarySearch(arr, data):
    arr.sort()
    return _binarySearch(arr, data)

def _binarySearch(arr, data):
    length = len(arr)
    currData = arr[int(length/2)] if length > 1 else arr[0]
    if data == currData:
        return True
    elif data < currData and length > 1:
        return _binarySearch(arr[:int(length/2)], data)
    elif data > currData and length > 1:
        return _binarySearch(arr[int(length/2):], data)
    else:
        return False

arr = [1, 3, 5, 7]
print(binarySearch(arr, 1))
print(binarySearch(arr, 3))
print(binarySearch(arr, 5))
print(binarySearch(arr, 7))
print(binarySearch(arr, -1))
print(binarySearch(arr, 4))
print(binarySearch(arr, 9))
