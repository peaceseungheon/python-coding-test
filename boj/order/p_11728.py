from sys import stdin, stdout

read = stdin.readline
write = stdout.write

N, M = map(int, read().rstrip().split())

A = list(map(int, read().rstrip().split()))
B = list(map(int, read().rstrip().split()))

arr = []
a_index = 0
b_index = 0

while a_index < N and b_index < M:
  candi_a = A[a_index]
  candi_b = B[b_index]
  
  if candi_a < candi_b:
    arr.append(candi_a)
    a_index += 1
  else:
    arr.append(candi_b)
    b_index += 1
  
if a_index != N:
  arr.extend(A[a_index:])
else:
  arr.extend(B[b_index:])

write(' '.join(map(str, arr)))