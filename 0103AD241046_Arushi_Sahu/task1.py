def count_palindromes(s):
    count = 0

    for i in range(len(s)):
        left = i
        right = i

        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

        left = i
        right = i + 1

        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

    return count


s = input()
print(count_palindromes(s))
