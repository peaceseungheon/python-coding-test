from itertools import permutations
import sys 
N = int(input())

nums = list(map(int, input().split()))

permu = list(permutations(nums, N))

answer = -sys.maxsize - 1

for p in permu:
  num_sum = 0
  for i in range(N-1):
    result = abs(p[i] - p[i+1])
    num_sum += result
  answer = max(answer, num_sum)
  
print(answer)