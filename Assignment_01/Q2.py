s = input("Enter string: ")

n = len(s)

start = 0
end = 0
maxLen = 0

for i in range(n):

    # Odd length palindrome
    l = i
    r = i

    while l >= 0 and r < n and s[l] == s[r]:

        length = r - l + 1

        if length > maxLen:
            maxLen = length
            start = l
            end = r

        l -= 1
        r += 1

    # Even length palindrome
    l = i
    r = i + 1

    while l >= 0 and r < n and s[l] == s[r]:

        length = r - l + 1

        if length > maxLen:
            maxLen = length
            start = l
            end = r

        l -= 1
        r += 1

print("Longest Palindrome:", s[start:end+1])
print("Start Index:", start)
print("End Index:", end)
print("Indices:", [start, end])