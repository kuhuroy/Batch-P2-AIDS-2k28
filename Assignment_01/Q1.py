# s = input("Enter String: ")
# count =0
# for i in range(len(s)):

#     l=i
#     r=i
#     while l>=0 and r<len(s) and s[l]==s[r]:
#         count+=1

#         l-=1
#         r+=1

#      #Even length
#         l=i
#         r=i+1

#     while l>=0 and r<len(s) and s[l] == s[r]:
#         count+=1
#         l-=1
#         r+=1

# print("Total Palindromic Substring:",count)

s = input("Enter String: ")
count = 0

for i in range(len(s)):

    # Odd length
    l = i
    r = i

    while l >= 0 and r < len(s) and s[l] == s[r]:
        count += 1
        l -= 1
        r += 1

    # Even length
    l = i
    r = i + 1

    while l >= 0 and r < len(s) and s[l] == s[r]:
        count += 1
        l -= 1
        r += 1

print("Total Palindromic Substrings:", count)