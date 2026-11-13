# given 2 strings s = some string, t = with blanck spot we have to fill that blanck spot
# input : t = "Fi_er", s = "Filler:Filter:Fiber:tailor:Fixer"
# output: Filer:Fiber:fixer

s = input()
t = input()

# s = "Filer:Filter:Fiber:tailor:Fixer"
# t = "Fi_er"

s = s.upper()
t = t.upper()
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

