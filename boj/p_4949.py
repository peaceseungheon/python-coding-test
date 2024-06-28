
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

while True:
  s = input()
  if s == '.':
    break
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
