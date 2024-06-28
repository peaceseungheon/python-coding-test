<<<<<<< HEAD

tokens = ['(', ')', '[', ']']

def smallAppendOrPop(stack: list, token: str):
  if token == '(':
    stack.append(token)
  else:
    if '(' in stack: stack.pop()
    
def bigAppendOrPop(stack: list, token: str):
  if token == '[':
    stack.append(token)
  else:
    if '[' in stack: stack.pop()

s_list = []
=======
from collections import deque

tokens = ['(', ')', '[', ']']

answers = []
>>>>>>> 2646eb360c727e0c35ccd5474b18c49149682037

while True:
  s = input()
  if s == '.':
    break
<<<<<<< HEAD
  s_list.append(s)
  
  s_list.
for s in s_list:
  small_stack = []
  big_stack = []
  for token in s:
    if token not in tokens:
      continue
    if token in ['(', ')']: smallAppendOrPop(small_stack, token)
    else: bigAppendOrPop(big_stack, token)
  if len(small_stack) == 0 and len(big_stack) == 0:
    print('yes')
  else:
    print('no')
=======
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
      
  
  
  
  
>>>>>>> 2646eb360c727e0c35ccd5474b18c49149682037
