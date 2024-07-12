from sys import stdin

read = stdin.readline

N, M = map(int, read().rstrip().split())
A = list(map(int, read().rstrip().split()))

i = 0
j = i

ans = 0
while i < N:
  
  if j >= N:
    i += 1
    j = i + 1
    continue
  
  result = sum(A[i:j+1])
  
  if result > M:
    i += 1
    j = i
  elif result < M:
    j += 1
  else:
    ans += 1
    i += 1
    j = i
    
print(ans)
