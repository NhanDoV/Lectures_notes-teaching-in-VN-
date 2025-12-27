# Calculate minimum run length (kept small here for demo)
def calcMinRun(n, minRUN = 32):
    r = 0
    while n >= minRUN:
        r |= n & 1
        n >>= 1
    return n + r

# Insertion sort for small ranges
def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Merge two sorted subarrays [l..m] and [m+1..r]
def merge(arr, l, m, r):
    left = arr[l:m+1]
    right = arr[m+1:r+1]
    i = j = 0
    k = l
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

# Detect ascending/descending run starting at index "start"
def findRun(arr, start, n):
    end = start + 1
    if end == n: return end
    if arr[end] < arr[start]:
        # descending
        while end < n and arr[end] < arr[end - 1]:
            end += 1
        arr[start:end] = reversed(arr[start:end])
    else:
        # ascending
        while end < n and arr[end] >= arr[end - 1]:
            end += 1
    return end

def Timsort(arr):
    n = len(arr)
    minRun = calcMinRun(n)
    runs = []

    i = 0
    while i < n:
        runEnd = findRun(arr, i, n)
        runLen = runEnd - i

        if runLen < minRun:
            end = min(i + minRun, n)
            insertionSort(arr, i, end - 1)
            runEnd = end

        runs.append((i, runEnd))
        i = runEnd

        while len(runs) > 1:
            l1, r1 = runs[-2]
            l2, r2 = runs[-1]
            len1, len2 = r1 - l1, r2 - l2
            if len1 <= len2:
                merge(arr, l1, r1 - 1, r2 - 1)
                runs.pop()
                runs[-1] = (l1, r2)
            else:
                break

    while len(runs) > 1:
        l1, r1 = runs[-2]
        l2, r2 = runs[-1]
        merge(arr, l1, r1 - 1, r2 - 1)
        runs.pop()
        runs[-1] = (l1, r2)

    return arr

# minRUN = 32
# Timsort(arr)