# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A, B, K):
    if A % K == 0:
        return -(-(B - A + 1) // K)
    else:
        return -(-(B - A + 1 - (K - (A % K))) // K)


print(solution(6, 11, 2))  # 3
print(solution(7, 14, 3))  # 2
print(solution(7, 15, 3))  # 3
