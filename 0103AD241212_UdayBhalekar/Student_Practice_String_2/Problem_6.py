# s = "aAbBCdD"

s = input()

m = {}
for c in s:
    m[c.lower()] = m.get(c.lower(),0)+1

f = False
ans = ""
for c in s:
    if(m[c.lower()] == 1):
        ans = c
        f = True
        break

if f is True:
    print(ans)
else :
    print("No unique character")