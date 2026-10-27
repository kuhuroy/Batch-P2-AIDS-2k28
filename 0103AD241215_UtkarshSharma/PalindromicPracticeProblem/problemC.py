
def count_long_palindrome_centers(s):
    n = len(s)
    count = 0

    for center in range(n):
        left = center
        right = center

        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1

        # Length of the longest palindrome at this center
        length = right - left - 1

        if length >= 3:
            count += 1

    return count


print(count_long_palindrome_centers("abcd"))    # 0
print(count_long_palindrome_centers("aba"))     # 1
print(count_long_palindrome_centers("ababa"))   # 3
print(count_long_palindrome_centers("abcbaxyx"))# 2
