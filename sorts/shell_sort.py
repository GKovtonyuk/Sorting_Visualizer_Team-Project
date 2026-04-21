def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                # 1. Показуємо порівняння та зсув
                yield j, j - gap, 0, n - 1
                arr[j] = arr[j - gap]
                j -= gap
            
            arr[j] = temp
            # 2. ОБОВ'ЯЗКОВО додаємо yield тут, щоб побачити фінальну вставку temp
            yield j, i, 0, n - 1
            
        gap //= 2
