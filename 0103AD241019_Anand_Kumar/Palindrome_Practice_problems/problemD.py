
def shortest_palindrome(s):
    rev = s[::-1]

    # Combine original string and its reverse
    temp = s + "#" + rev

    # Build LPS (Longest Prefix Suffix) array
    lps = [0] * len(temp)

    j = 0
    for i in range(1, len(temp)):
        while j > 0 and temp[i] != temp[j]:
            j = lps[j - 1]

        if temp[i] == temp[j]:
            j += 1

        lps[i] = j

    # Length of the longest palindromic prefix
    k = lps[-1]

    # Add the reverse of remaining characters
    return rev[:len(s) - k] + s


print(shortest_palindrome("aba"))
print(shortest_palindrome("aacecaaa"))
print(shortest_palindrome("abb"))
print(shortest_palindrome("abcd"))
