def heapify(arr, n, i):    
    largest = i        # Initialize largest as root
    l = 2 * i + 1      # left index = 2*i + 1
    r = 2 * i + 2      # right index = 2*i + 2

    if l < n and arr[l] > arr[largest]:      # If left child is larger than root
        largest = l

    if r < n and arr[r] > arr[largest]:     # If right child is larger than largest so far
        largest = r

    if largest != i:                        # If largest is not root
        arr[i], arr[largest] = arr[largest], arr[i]   # swap
        heapify(arr, n, largest)                      # Recursively heapify the affected sub-tree  

def HeapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr
