# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    sum_left = A[0]
    sum_right = sum(A) - sum_left
    result = abs(sum_left - sum_right)

    for i in range(1, len(A) - 1):
        sum_left += A[i]
        sum_right -= A[i]
        result = min(result, abs(sum_left - sum_right))

    return result


# print(solution([3, 1, 2, 4, 3]))
