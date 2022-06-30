# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(S, P, Q):

    # ACGT の変化を求めておく
    change_amount = [[0] * (len(S) + 1) for i in range(4)]
    for i in range(1, len(S) + 1):
        for j in range(4):
            change_amount[j][i] = change_amount[j][i - 1]

        if S[i - 1] == "A":
            change_amount[0][i] += 1
        elif S[i - 1] == "C":
            change_amount[1][i] += 1
        elif S[i - 1] == "G":
            change_amount[2][i] += 1
        elif S[i - 1] == "T":
            change_amount[3][i] += 1

    result = []

    for i in range(len(P)):
        for j in range(4):
            if 0 < (change_amount[j][Q[i] + 1] - change_amount[j][P[i]]):
                result.append(j + 1)
                break

    return result

    # TLE
    # s_number = []

    # for i in S:
    #     if i == "A":
    #         s_number.append(1)
    #     elif i == "C":
    #         s_number.append(2)
    #     elif i == "G":
    #         s_number.append(3)
    #     elif i == "T":
    #         s_number.append(4)

    # result = []
    # for i in range(len(P)):
    #     _s = s_number[P[i] : (Q[i] + 1)]
    #     result.append(min(_s))

    # return result


print(solution("CAGCCTA", [2, 5, 0], [4, 5, 6]))  # [2, 4, 1]
