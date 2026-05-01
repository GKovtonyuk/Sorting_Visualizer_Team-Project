def double_selection_sort(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        min_idx, max_idx = left, left
        for i in range(left, right + 1):
            yield min_idx, max_idx, left, right
                if arr[i] < arr[min_idx]:
                min_idx = i
            if arr[i] > arr[max_idx]:
                max_idx = i
        arr[left], arr[min_idx] = arr[min_idx], arr[left]
        if max_idx == left:
            max_idx = min_idx
        arr[right], arr[max_idx] = arr[max_idx], arr[right]
        left += 1
        right -= 1