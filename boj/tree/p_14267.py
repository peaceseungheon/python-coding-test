# counts 배열을 만든다

'''
직원번호 i가 주어지면,
1. counts[i]에 w를 더해준다.
2. i의 하위 직원들의 counts에 w를 더해준다.
'''
from sys import stdin
read = stdin.readline

N, M = list(map(int, read().rstrip().split()))

parents = list(map(int, read().rstrip().split()))
counts = [0] * (N+1)

for _ in range(M):
  i, w = list(map(int, read().rstrip().split()))
  
  counts[i] += w
  
  parent = i
  for j in range(1, N+1):
    if parents[j-1] == parent:
      counts[j] += w
      parent = j

print(' '.join(map(str, counts[1:])))
  