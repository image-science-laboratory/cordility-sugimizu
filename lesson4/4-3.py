# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(N, A):
    dic = {i + 1: 0 for i in range(N)}
    max_value = 0
    temp_max_value = 0

    for i in A:
        # A[K] = N + 1 → max counter
        if i == (N + 1):
            max_value = temp_max_value

        else:
            dic[i] = max(max_value, dic[i]) + 1
            temp_max_value = max(temp_max_value, dic[i])

    # 最低値を最大値に
    for i in range(N):
        dic[i + 1] = max(max_value, dic[i + 1])

    return list(dic.values())


print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
