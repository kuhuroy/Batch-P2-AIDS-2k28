
s = input("Enter string: ")

start = 0
end = 0

for center in range(len(s)):

    # Odd length
    left = center
    right = center

    while left >= 0 and right < len(s) and s[left] == s[right]:
        if right - left > end - start:
            start = left
            end = right

        left -= 1
        right += 1

    # Even length
    left = center
    right = center + 1

    while left >= 0 and right < len(s) and s[left] == s[right]:
        if right - left > end - start:
            start = left
            end = right

        left -= 1
        right += 1

print("Start index:", start)
print("End index:", end)
print("Palindrome:", s[start:end+1])
