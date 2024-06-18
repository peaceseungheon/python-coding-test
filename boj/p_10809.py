def getNum(char):
  return ord(char) - ord('a')

def solution(s: str):
  count = [-1] * 26
  
  s_len = len(s)
  if s_len == 0:
    return count
  for i in range(s_len):
    index = getNum(s[i])
    if(count[index] == -1):
      count[index] = i
  return count
  

s = input()

count = solution(s)

print(' '.join(list(map(lambda x: str(x), count)))) 
