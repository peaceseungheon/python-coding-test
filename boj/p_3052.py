x_set = set()

for _ in range(10):
  n = int(input())
  x_set.add(n % 42)
  
print(len(x_set))
  