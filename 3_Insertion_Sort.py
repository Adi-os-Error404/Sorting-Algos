
def insertionSort(arr, n):

    for i in range(1, n):

        key = arr[i]
        j = i-1

        while arr[j] > key and j >= 0:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

    return arr


arr = [12,7,5,13,6,2,4]
print(insertionSort(arr, len(arr)))
