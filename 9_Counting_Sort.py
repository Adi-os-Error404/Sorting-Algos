
def countingSort(arr):
    u = max(arr) + 1
    n = len(arr)

    counter = [0] * u
    for num in arr:
        counter[num] += 1
    
    # Create a position array to store the starting position of each element in the sorted array
    pos = [0] * u
    pos[0] = 1
    for i in range(1, u):
        pos[i] = pos[i-1] + counter[i-1]


    sorted = [0] * n
    for num in arr:
        sorted[pos[num]-1] = num
        pos[num] += 1


    return sorted



arr = [1,12,7,1,5,13,6,2,4]
print(countingSort(arr))