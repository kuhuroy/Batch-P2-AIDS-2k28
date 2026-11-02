def isPal(s): 
    n = len(s)
    for i in range(0,n): 
        if(s[i] != s[n-i-1]):
            return False
    return True

s = input()

n = len(s)
f = 0
l = 0
ans = ""
while(True): 
    if(isPal(s)): 
        break
    t = len(s)-1
    ans += s[t-l]
    s = s[:f]+s[t-l]+s[f:]
    f += 1
    l += 1
print(ans)