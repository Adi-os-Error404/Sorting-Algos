
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    A = mergeSort(arr[:mid])
    B = mergeSort(arr[mid:])
    return merge(A, B )


def merge(A, B):
    i, j = 0, 0
    merged = []

    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            merged.append(A[i])
            i+=1
        else:
            merged.append(B[j])
            j+=1

    return merged + A[i:] + B[j:]


arr = [12,7,5,13,6,2,4]
print(mergeSort(arr))
