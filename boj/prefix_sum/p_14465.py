import sys
N, K, B = list(map(int, input().split()))

arr = [0] * N

# 고장난 index를 1로 바꾼다.

for _ in range(B):
  b = int(input())
  arr[b-1] = 1
  
# 누적합을 구한다
p_sum = [0] * N
for i in range(N):
  if i == 0:
    p_sum[i] = arr[i]
  else:
    p_sum[i] = p_sum[i-1] + arr[i]
    
# 연속한 K만큼의 구간을 확인하며 구간의 합이 가장 작은 것으로 갱신해준다.
ans = sys.maxsize
for i in range(0, N-K):
  if i == 0:
    ans = min(ans, p_sum[i+K])
  else:
    ans = min(ans, (p_sum[i+K] - p_sum[i]))

print(ans)

