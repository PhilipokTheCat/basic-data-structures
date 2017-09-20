def countedSort(arr):
    length = len(arr)
    helpArr = [0]*length
    for elem in arr: helpArr[elem] += 1
    temp = 0
    for i in range(length):
        if helpArr[i] > 0:
            arr[temp:temp + helpArr[i]] = [i]*helpArr[i]
            temp += helpArr[i]
    return arr

arr = [7, 3, 5, 5, 3, 7, 7, 3, 5, 5]
arr = countedSort(arr)
print(arr)