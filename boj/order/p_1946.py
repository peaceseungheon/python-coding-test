from sys import stdin, stdout
from operator import itemgetter

read = stdin.readline
write = stdout.write

test_case_num = int(read().rstrip())

for _ in range(test_case_num):
  N = int(read().rstrip())
  
  orders = []
  
  for i in range(N):
    order = map(int, read().rstrip().split())
    orders.append(tuple(order))
    
  orders.sort(key= itemgetter(0))
  answer = 0
  
  high_of_second = 1000001
  
  for i in range(N):
    order = orders[i]
    high_of_second = min(high_of_second, order[1])
    
    # 1차, 2차 면접 순위가 1등이면 무조건 뽑힘
    if order[0] == 1 or order[1] == 1:
      answer += 1
      continue
    
    # 지금까지 나온 2차면접 최고 순위가 비교 대상의 면접 순위보다 높으면 비교 대상은 못 뽑힘
    if high_of_second < order[1]:
      continue
    
    answer += 1
  
  print(answer)
  