# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    count = 0
    add = sum(A)

    for i in A:
        if i == 0:
            count += add
        else:
            add -= 1

        # count が 10**9 超えた場合 -1 を返す
        if 10**9 < count:
            return -1

    return count


print(solution([0, 1, 0, 1, 1]))  # 5
