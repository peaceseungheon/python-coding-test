from sys import stdin

read = stdin.readline

T = int(read().rstrip())

for _ in range(T):
  N, M = list(map(int, read().rstrip().split()))
  
  A = list(map(int, read().rstrip().split()))
  B = list(map(int, read().rstrip().split()))
  
  A.sort(reverse= True)
  B.sort()
  
  ans = 0
  
  a_index = 0
  b_index = len(B) - 1
  
  while a_index < len(A) and b_index >= 0:
    a_top = A[a_index]
    b_top = B[b_index]
    
    if a_top > b_top:
      ans += len(B[0:b_index+1])
      a_index += 1
      continue
    else:
      b_index -= 1
  print(ans)