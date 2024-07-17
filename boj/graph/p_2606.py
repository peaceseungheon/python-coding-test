from sys import stdin
read = stdin.readline

N = int(read().rstrip())
M = int(read().rstrip())

abj = [[] for _ in range(N)]

for _ in range(M):
  i, j = list(map(int, read().rstrip().split()))
  abj[i-1].append(j-1)
  abj[j-1].append(i-1)

is_virused = [0] * N
checked = [0] * N
def virus(abj, is_virused, node):
  if checked[node] == 1:
    return
  checked[node] = 1
  
  nodes = abj[node]
  for n in nodes:
    if is_virused[n] == 0:
      is_virused[n] = 1
  
  for n in nodes:
    virus(abj, is_virused, n)
    
virus(abj, is_virused, 0)

print(sum(is_virused[1:]))