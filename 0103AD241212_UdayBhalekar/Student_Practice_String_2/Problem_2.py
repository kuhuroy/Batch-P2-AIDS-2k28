
t = input()
s = input()

# s = "care:code:cake:cope:case:cheese"
# t = "c__e"

t = t.upper()
s = s.upper()
lst = []
st = ""
for i in range(0,len(s)):
    if(s[i] == ':'):
        lst.append(st)
        st = ""
    else :
        st += s[i]

lst.append(st)

ans = ""
for val in lst:
    if(len(val) == len(t)):
        f = 0
        for i in range(0,len(t)):
            if(t[i] == '_') : 
                continue
            if(t[i] != val[i]): 
                f = 1 
                break
        if(f == 0) : 
            ans += val
            ans += ':'

print(ans[:-1]) 

