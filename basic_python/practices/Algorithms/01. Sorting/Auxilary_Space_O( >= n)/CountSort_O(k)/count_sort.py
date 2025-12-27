def CountSort(arr):
    if not arr:
        return []

    n = len(arr)
    maxval = max(arr)

    cntArr = [0] * (maxval + 1)         # initialize cntArr

    for v in arr:                       # count frequency of each element
        cntArr[v] += 1

    for i in range(1, maxval + 1):      # compute prefix sums
        cntArr[i] += cntArr[i - 1]

    # build output array
    ans = [0] * n
    for i in range(n - 1, -1, -1):
        v = arr[i]
        ans[cntArr[v] - 1] = v
        cntArr[v] -= 1

    return ans

# CountSort(arr)