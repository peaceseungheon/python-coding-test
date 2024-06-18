K = int(input())

stack = []

for _ in range(K):
  n = int(input())
  if n != 0:
    stack.append(n)
  else:
    if len(stack) != 0:
      stack.pop()

sum = 0
for n in stack:
  sum += n

print(sum)