from collections import deque

# 상근의 친구와 친구의 친구까지만 초대

N = int(input())
M = int(input())

abj = [[] for _ in range(N)]

for _ in range(M):
  i, j = list(map(int, input().split()))
  abj[i-1].append(j-1)
  abj[j-1].append(i-1)

checked = [0] * N

sg_friends = abj[0]

stack = deque()

stack.extend(sg_friends)

for f in sg_friends:
  stack.extend(abj[f])

while len(stack) != 0:
  friend = stack.pop()
  if checked[friend] == 1:
    continue
  checked[friend] = 1
print(sum(checked[1:]))

'''
# 상근 친구들 초대
for i in sg_friends:
  checked[i] = 1

# 상근 친구들의 친구들 초대

for f in sg_friends:
  for j in abj[f]:
    if checked[j] == 1:
      continue
    checked[j] = 1
    
print(sum(checked[1:]))
'''