
s = input("Enter string: ")

count = 0

for center in range(len(s)):

    # Odd length palindrome
    left = center
    right = center

    while left >= 0 and right < len(s) and s[left] == s[right]:
        count += 1
        left -= 1
        right += 1

    # Even length palindrome
    left = center
    right = center + 1

    while left >= 0 and right < len(s) and s[left] == s[right]:
        count += 1
        left -= 1
        right += 1

print("Total palindromes:", count)
