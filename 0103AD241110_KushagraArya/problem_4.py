#frequency of all elemments in a list 
l = [ 1,2,3,2,1,4,2,5,2,5,3,3,4,8,6,]
freq = {}
for i in l :
    if i  in freq:
        freq[i]+=1
    else:
        freq[i] = 1
print(freq)        
