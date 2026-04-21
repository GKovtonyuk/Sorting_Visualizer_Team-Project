def sort(arr):
    ops = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            ops += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return ops
