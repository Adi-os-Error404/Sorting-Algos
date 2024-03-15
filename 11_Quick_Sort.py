import math


#-----------------------------------------------------------------------------------
def naive_partition(arr, piv_idx):
    pivot = arr[piv_idx]
    left, pivots, right = [],[],[]

    for i in range(len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        elif arr[i] == pivot:
            pivots.append(arr[i])
        else:
            right.append(arr[i])

    temp = left+pivots+right
    for i in range(len(arr)): arr[i] = temp[i]

    partitioning_idx =  len(left) + math.ceil((len(pivots)//2))
    return partitioning_idx

arr = [6,2,8,7,1,3,4,5]
idx = naive_partition(arr, 6) # pivot: 4
print('\nNaive Partition: ' + str(arr) + '\nPartition at idx: ' + str(idx))


#-----------------------------------------------------------------------------------
def hoare_partition(arr, piv_idx):
    arr[0],arr[piv_idx] = arr[piv_idx],arr[0]
    i, j = 1, len(arr)-1

    while (i <= j):
        while (i<=j) and (arr[i] <= arr[0]):    i+= 1
        while (i<=j) and (arr[j] > arr[0]):     j-= 1

        if (i<=j):  arr[i],arr[j] = arr[j],arr[i]

    arr[0],arr[j] = arr[j],arr[0]

    return j

arr = [6,2,8,7,1,3,4,5]
idx = hoare_partition(arr, 6) # pivot: 4
print('\nHoare Partition: ' + str(arr) + '\nPartition at idx: ' + str(idx))


#-----------------------------------------------------------------------------------
def dnf(arr, piv_idx):
    pivot = arr[piv_idx]
    lo, mid, hi = 0, 0, len(arr)-1


    while mid <= hi:
        if arr[mid] > pivot: # RED
            arr[mid],arr[hi] = arr[hi],arr[mid]
            hi -= 1

        elif arr[mid] < pivot: #BLUE
            arr[mid],arr[lo] = arr[lo],arr[mid]
            lo += 1
            mid += 1
        
        else: #WHITE
            mid += 1
            
    return lo, mid-1

arr = [6,2,8,7,1,3,4,5]
i, j = dnf(arr, 6) # pivot: 4
print('\nDNF Partition: ' + str(arr) + '\nPartition at idx: ' + str(i) + ', ' +str(j))


#-----------------------------------------------------------------------------------
def quickSort(arr, lo= None, hi= None):
    if lo is None:  lo = 0
    if hi is None:  hi = len(arr) - 1

    if hi > lo:
        piv_idx = lo
        mid = naive_partition(arr, piv_idx)
        quickSort(arr, lo, mid-1)
        quickSort(arr, mid+1, hi)



arr = [6,2,8,7,1,3,4,5]
print('\n\nSort arr:', arr)
quickSort(arr)
print('Sorted arr:', arr)



