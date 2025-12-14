import time

def using_swap(arr: list[float]) -> list[float]:
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

if __name__ == "__main__":
    n = int( input("input length of your array:") )
    arr = []
    for _ in range(n):
        arr.append( float( input(f"\t element {_ + 1}: ") ) )
    print("Your input:")
    print(arr)
    print('Swap-Sort results:')
    t0 = time.time()
    res = using_swap(arr)
    print(res)
    print(f"Ellapsed time: {(time.time() - t0)}")