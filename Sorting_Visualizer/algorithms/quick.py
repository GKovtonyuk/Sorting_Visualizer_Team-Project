def sort(arr):
    ops = 0

    def quicksort(a, low, high):
        nonlocal ops
        if low < high:
            pi = partition(a, low, high)
            quicksort(a, low, pi - 1)
            quicksort(a, pi + 1, high)

    def partition(a, low, high):
        nonlocal ops
        pivot = a[high]
        i = low - 1
        for j in range(low, high):
            ops += 1
            if a[j] < pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
        a[i + 1], a[high] = a[high], a[i + 1]
        return i + 1

    quicksort(arr, 0, len(arr) - 1)
    return ops
