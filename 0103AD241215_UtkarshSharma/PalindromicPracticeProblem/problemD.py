
def shortest_palindrome(s):
    n = len(s)

    if n == 0:
        return s

    longest_prefix_end = 0

    for center in range(n):

        # Odd-length palindromes
        left = center
        right = center

        while left >= 0 and right < n and s[left] == s[right]:
            if left == 0:
                longest_prefix_end = right

            left -= 1
            right += 1

        # Even-length palindromes
        left = center
        right = center + 1

        while left >= 0 and right < n and s[left] == s[right]:
            if left == 0:
                longest_prefix_end = right

            left -= 1
            right += 1

    # Characters after the longest palindromic prefix
    suffix = s[longest_prefix_end + 1:]

    # Reverse the suffix and add it to the front
    return suffix[::-1] + s


print(shortest_palindrome("aba"))       # aba
print(shortest_palindrome("aacecaaa"))  # aaacecaaa
print(shortest_palindrome("abb"))       # bbabb
print(shortest_palindrome("abcd"))      # dcbabcd
