from collections import deque

tokens = ['(', ')', '[', ']']

answers = []

while True:
  s = input()
  if s == '.':
    break
  stack = deque()
  balanced = True

  for token in s:
    if token not in tokens:
      continue
    
    if len(stack) == 0:
      stack.append(token)
      continue
  
    if token in ['(', '[']:
      stack.append(token)
      continue
    
    last  = stack[-1]
    if token == ')':
      if last == '(':
        stack.pop()
      else:
        balanced = False
        break
    
    if token == ']':
      if last == '[':
        stack.pop()   
      else:
        balanced = False
        break
          
  if len(stack) == 0 and balanced:
    print('yes')
  else:
    print('no')
      
  
  
  
  