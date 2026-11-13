# s = "                    Java         is          Easy"
# t = "        java         is                     easy               "

s = input()
t = input()

s = s.lower()
t = t.lower()
s = s.strip()
t = t.strip()

ss, tt = "", ""


for i in range(len(s)-1):
    if(s[i] == ' ' and s[i+1] == ' '):
        continue
    else : 
        ss += s[i]
for i in range(len(t)-1):
    if(t[i] == ' ' and t[i+1] == ' '):
        continue
    else : 
        tt += t[i]

n, m = len(s)-1, len(t)-1
if(s[n] != ' '):
    ss += s[n] 

if(t[m] != ' '):
    tt += t[m]     
        
if(ss == tt):
    print("MATCH")
else:
    print("NOT-MATCH")