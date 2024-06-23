from collections import deque
import sys

read = sys.stdin.readline
write = sys.stdout.write

N = int(read().rstrip())
arr = deque()

for _ in range(N):
  tokens = read().rstrip().split(' ')
  
  cmd = tokens[0]
  arr_len = len(arr)
  
  if cmd == 'push':
    param = int(tokens[1])
    arr.append(param)
  
  if cmd == 'pop':
    if arr_len == 0:
      write('-1 \n')
    else:
      write(str(arr.popleft()) + '\n')
  
  if cmd == 'size':
    write(str(arr_len) + '\n')
  
  if cmd == 'empty':
    if arr_len == 0:
      write('1\n')
    else:
      write('0\n')
  
  if cmd == 'front':
    if arr_len == 0:
      write('-1\n')
    else:
      write(str(arr[0]) + '\n')
  
  if cmd == 'back':
    if arr_len == 0:
      write('-1\n')
    else:
      write(str(arr[-1]) + '\n')