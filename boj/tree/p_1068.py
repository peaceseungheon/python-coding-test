from sys import stdin

read = stdin.readline

N = int(read().rstrip())

parents = list(map(int, read().rstrip().split()))

childs = [[] for _ in range(N)]

#parents: -1 0 0 1 1
#childs: [1,2], [3, 4], [], [], []
for i in range(N):
  if parents[i] == -1:
    continue
  childs[parents[i]].append(i)
  
def delete(delete_node, childs):
  temp = childs[delete_node]
  childs[delete_node] = None
  
  if len(temp) == 0:
    return
  else:
    for n in temp:
      delete(n, childs)
  

delete_node = int(read().rstrip())

for arr in childs:
  if delete_node in arr:
    arr.remove(delete_node)
    break

delete(delete_node, childs)

ans = 0
for arr in childs:
  if arr is None:
    continue
  if len(arr) == 0:
    ans += 1

print(ans)