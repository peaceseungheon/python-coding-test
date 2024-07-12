from sys import stdin

read = stdin.readline

N = int(read().rstrip())

arr = []

for _ in range(N):
  arr.append(int(read().rstrip()))

ans = 0
# N = 4
# 5 3 7 5 -> i == 2) 5 3 4 5 -> 5 3 4 5 -> 2 3 4 5
for i in range(N-2, -1, -1):
  if arr[i] >= arr[i+1]:
    diff = arr[i] - arr[i+1] + 1
    arr[i] = arr[i] - diff
    ans += diff

print(ans)
