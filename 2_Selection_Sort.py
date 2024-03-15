
def selectionSort(arr, n):

    for i in range(n):
        min = i
        
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j

        arr[i], arr[min] = arr[min], arr[i]

    return arr


arr = [12,7,5,13,6,2,4]
print(selectionSort(arr, len(arr)))
