N = int(input())

A = list(map(int, input().split()))
A.sort()

M = int(input())

find_nums = list(map(int, input().split()))

def search(find: int, arr: list):
  
  left_index = 0
  right_index = len(arr) -1
  
  find_index = -1

  
  while left_index <= right_index:
    
    mid_index = (left_index + right_index) // 2
    
    if arr[mid_index] == find:
      find_index = mid_index
      break
    elif arr[mid_index] < find:
      left_index = mid_index + 1
    else:
      right_index = mid_index - 1
      
  return find_index

for n in find_nums:
  index = search(n, A)
  
  if index == -1:
    print(0)
  else:
    print(1)
  
