N = int(input())

requests = list(map(lambda x: int(x), input().split(' ')))

budget = int(input())

max_req = 0
for n in requests:
  max_req = max(max_req, n)

# 탐색범위: 0 ~ limi

sum_req = sum(requests)

if sum_req <= budget:
  print(max_req)
else:
  left = 0
  right = max_req
  answer = 0
  while left <= right:
    
    middle = (left + right) // 2
    
    sum = 0
    for i in range(N):
      sum += min(middle, requests[i])
    
    if sum <= budget:
      answer = middle
      left = middle + 1
    else:
      right = middle - 1
      

  print(answer)
  
    
