# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(X, A):
    data = {}

    for i in range(len(A)):
        if A[i] not in data:
            data[str(A[i])] = 1

        if len(data) == X:
            return i

    return -1


print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))  # 6
print(solution(2, [2, 2, 2, 2, 2, 2, 2, 2]))  # -1
print(solution(3, [1, 3, 1, 3, 2, 1, 3]))  # 4
