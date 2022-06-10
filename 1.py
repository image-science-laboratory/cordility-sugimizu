def solution(N):
  # 2進数への変換
  binary_number = bin(N)
  binary_number = binary_number[2::]

  binary_gap = 0
  max_binary_gap = 0

  for i in range(len(binary_number)):
    if binary_number[i] == "1":
      if max_binary_gap < binary_gap:
        max_binary_gap = binary_gap
      binary_gap = 0
    else:
      binary_gap += 1
    
  return max_binary_gap