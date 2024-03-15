
def countInversions(arr):
    if len(arr) <= 1:
        return (arr, 0)
    
    mid = (len(arr)//2)

    A, invA = countInversions(arr[:mid])
    B, invB = countInversions(arr[mid:])
    M, invM = merge(A, B)

    return (M, (invA+invB+invM))


def merge(A, B):
    i, j = 0, 0
    merged, inv = [], 0

    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            merged.append(A[i])
            i+=1
        else:
            inv += len(A) - j
            merged.append(B[j])
            j+=1

    return ((merged + A[i:] + B[j:]), inv)


arr = [1,3,4,2,7,0]
print(countInversions(arr))
