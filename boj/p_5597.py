submitted = list(map(lambda x: False, range(30)))

for i in range(28):
  n = int(input())
  submitted[n-1] = True
    
for i in range(len(submitted)):
  if submitted[i] == False:
    print(i+1)