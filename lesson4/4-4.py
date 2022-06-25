# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    dic = {}

    for i in A:
        if i not in dic:
            dic[i] = True

    for i in range(1, len(dic) + 1):
        if i not in dic:
            return i

    return len(dic) + 1


print(solution([1, 3, 6, 4, 1, 2]))  # 5
print(solution([1, 2, 3]))  # 4
print(solution([-1, -3]))  # 1
