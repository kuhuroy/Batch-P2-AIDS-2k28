s = input("Enter string: ")

n = len(s)
count = 0

for i in range(n):

    l = i
    r = i

    found = False

    while l >= 0 and r < n and s[l] == s[r]:

        length = r - l + 1

        if length >= 3:
            found = True

        l -= 1
        r += 1

    if found:
        count += 1

print("Centers with palindrome length >= 3:", count)