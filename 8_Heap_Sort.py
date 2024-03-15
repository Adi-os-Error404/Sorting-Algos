class MaxHeap:
    
    def __init__(self):
        self.heap = [None]


    def heapify(self, array):
        self.heap += array
        n = len(self.heap) - 1
        for i in range(n // 2, 0, -1):
            self.fall(i)

    def insert(self, x):
        self.heap.append(x)
        self.rise(len(self.heap) - 1)

    def extract_max(self):
        if len(self.heap) <= 1:
            return None
        self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
        max_value = self.heap.pop()
        self.fall(1)
        return max_value

    def rise(self, i):
        parent = i // 2
        while parent >= 1:
            if self.heap[parent] < self.heap[i]:
                self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
                i = parent
            else:
                break

    def fall(self, i):
        n = len(self.heap) - 1
        child = 2 * i
        while child <= n:
            if child < n and self.heap[child + 1] > self.heap[child]:
                child += 1
            if self.heap[i] < self.heap[child]:
                self.heap[i], self.heap[child] = self.heap[child], self.heap[i]
                i = child
            else:
                break


    def __str__(self) -> str:
        return str(self.heap)




def heapSort(array):
    heap = MaxHeap()
    heap.heapify(array)

    n = len(array)
    for i in range(n, 0, -1):
        print(i, arr, heap)
        array[i - 1] = heap.extract_max()

    return array


arr = [12,7,5,13,6,2,4]
print(heapSort(arr))
