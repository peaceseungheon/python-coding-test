import sys

N, K = list(map(int,input().split()))
arr = list(map(int, input().split()))

p_sum = [0] * N

for i in range(N):
  if i == 0:
    p_sum[i] = arr[i]
  else:
    p_sum[i] = p_sum[i-1] + arr[i]
  
ans = -sys.maxsize - 1

if K == N:
  print(p_sum[N-1])
else:
  for i in range(K-1, N, 1):
    if i-K < 0:
      ans = max(ans, p_sum[i])
    else:
      ans = max(ans, p_sum[i] - p_sum[i-K])
  print(ans)