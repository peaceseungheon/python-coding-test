# 7명의 키의 합이 100
from itertools import combinations

talls = []

for _ in range(9):
  tall = int(input())
  talls.append(tall)
  
com = list(combinations(talls, 7))

answer = None
for c in com:
  sum_talls = sum(c)
  if sum_talls == 100:
    answer = sorted(c)
    break


for a in answer:
  print(a)
