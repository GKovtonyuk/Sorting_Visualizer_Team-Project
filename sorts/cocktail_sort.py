def cocktail_sort(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        for i in range(start, end):
            yield i, i + 1, start, end
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        end -= 1

        for i in range(end, start, -1):
            yield i, i - 1, start, end
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        start += 1