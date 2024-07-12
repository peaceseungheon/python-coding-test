from sys import stdin

read = stdin.readline

N = int(read().rstrip())
arr = list(map(int, read().rstrip().split()))
arr.sort()
ans = 0

for i in range(N):
  ans += sum(arr[0:i+1])
  
print(ans)

