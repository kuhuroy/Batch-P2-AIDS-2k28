def isPal(s): 
    n = len(s)
    for i in range(0,n): 
        if(s[i] != s[n-i-1]):
            return False
    return True
   
s = input()

n = len(s)
mx = 0
ans = ""
for i in range(0,n):
    for j in range(i,n): 
        sub = s[i:j]
        if isPal(sub) and mx < len(sub):
            ans = sub
            mx = len(sub)
print(ans)