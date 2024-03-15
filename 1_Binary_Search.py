
def binarySearch(key, arr, n):
    lo = 0
    hi = n

    while lo < hi-1:
        mid = (lo+hi)//2
        if arr[mid] <= key:
            lo = mid
        else:
            hi = mid

    if arr[lo] == key: return lo
    else: return None


key, arr = 1, [0,1,2,3,4]
print(binarySearch(key, arr, len(arr)))
