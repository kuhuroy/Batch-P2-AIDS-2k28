def count_palindrome_centres(s):
    count = 0

    for i in range(len(s)):
        # Odd length palindrome
        left = i
        right = i

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        length = right - left - 1
        if length >= 3:
            count += 1

        # Even length palindrome
        left = i
        right = i + 1

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        length = right - left - 1
        if length >= 3:
            count += 1

    return count


print(count_palindrome_centres("abcd"))
