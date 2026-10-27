
def count_palindromes(s):
    count = 0
    n = len(s)

    for center in range(n):

        # Odd-length palindromes
        left = center
        right = center

        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

        # Even-length palindromes
        left = center
        right = center + 1

        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

    return count


print(count_palindromes("abc"))   # 3
print(count_palindromes("aba"))   # 4
print(count_palindromes("abba"))  # 6
print(count_palindromes("aaa"))   # 6
print(count_palindromes("xabay")) # 6
