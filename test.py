def perfectPeak(A):
    n = len(A)
    max_left = [0] * n
    min_right = [0] * n

    max = A[0]
    min = A[n - 1]
    for i in range(1, n + 1):
        if A[i - 1] > max:
            max = A[i - 1]
        max_left[i - 1] = max
        if A[n - i] < min:
            min = A[n - i]
        min_right[n - i - 1] = min

    for i in range(1, n):
        if max_left[i - 1] < A[i] < min_right[i]:
            return 1
    return 0


print(perfectPeak([2, 3, 2]))
