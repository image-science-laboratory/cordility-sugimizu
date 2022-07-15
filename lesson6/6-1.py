# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    dic = {}

    for i in A:
      if i not in dic:
        dic[i] = True

    return len(dic)

print(solution([2, 1, 1, 2, 3, 1]))