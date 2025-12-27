def partition(arr, low, high):
    pivot = arr[high]           # choose the pivot
    i = low - 1                 # index of smaller element and indicates  the right position of pivot found so far
    
    for j in range(low, high):  # traverse arr[low..high] and move all smaller elements to the left side. 
        if arr[j] < pivot:      # Elements from low to i are smaller after every iteration
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1] # move pivot after smaller elements and return its position
    return i + 1    

def QuickSort(arr, low, high):
    if low < high:
                
        pi = partition(arr, low, high)      # the partition return index of pivot
    
        QuickSort(arr, low, pi - 1)         # recursion calls for smaller elements 
        QuickSort(arr, pi + 1, high)        # and greater or equals elements
    return arr

# QuickSort(arr, 0, len(arr) - 1)