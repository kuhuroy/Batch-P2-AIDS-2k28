
def longest_palindrome_indices(s):
    n = len(s)
    start = 0
    end = 0

    for center in range(n):

        # Odd-length palindrome
        left = center
        right = center

        while left >= 0 and right < n and s[left] == s[right]:
            if right - left > end - start:
                start = left
                end = right

            left -= 1
            right += 1

        # Even-length palindrome
        left = center
        right = center + 1

        while left >= 0 and right < n and s[left] == s[right]:
            if right - left > end - start:
                start = left
                end = right

            left -= 1
            right += 1

    return [start, end]


print(longest_palindrome_indices("dabac"))   # [1, 3]
print(longest_palindrome_indices("cabbad"))  # [1, 4]
print(longest_palindrome_indices("xyzzyxab"))# [0, 5]
print(longest_palindrome_indices("abcd"))    # [0, 0]
