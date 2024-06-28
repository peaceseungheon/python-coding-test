from collections import deque

N = int(input())
  
def draw(arr: deque):
  arr.popleft()

def push(arr: deque):
  n = arr.popleft()
  arr.append(n)
  
arr = deque()

for i in range(N):
  arr.append(i + 1)

while True:
  
  if len(arr) == 1:
    break
  
  draw(arr)
  
  if len(arr) == 1:
    break
  
  push(arr)
  
print(arr[0])