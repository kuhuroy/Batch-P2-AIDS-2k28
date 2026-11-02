def isPal(s): 
    n = len(s)
    for i in range(0,n): 
        if(s[i] != s[n-i-1]):
            return False
    return True
  
s = input()

n = len(s)
cnt = 0
for i in range(0,n):
    for j in range(i,n): 
        sub = s[i:j]
        if isPal(sub):
            cnt = cnt+1
print(cnt)
