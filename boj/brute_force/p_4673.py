# 10001 개의 배열을 생성한다.
# n에 대해 1 ~ 10000까지 수열을 만들며 n으로 시작하는 수열이 이전의 수열 안에 포함되는지 확인
from sys import stdout


def d(n: int, sets: set):
  sets.add(n)
  if n > 10000:
    return
  nums = list(map(int, str(n)))
  nums_sum = n + sum(nums)
  sets.add(nums_sum)
  return d(nums_sum, sets)


sets = set()


n = 1
while n < 10000:
  if n not in sets:
    stdout.write(str(n) + '\n')
  d(n, sets)
  n += 1
  