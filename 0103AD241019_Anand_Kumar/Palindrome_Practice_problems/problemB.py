
def longestPalindrome(s):
    n = len(s)

    start = 0
    end = 0

    def expand(left, right):
        nonlocal start, end

        while left >= 0 and right < n and s[left] == s[right]:
            # Update if we find a longer palindrome
            if right - left > end - start:
                start = left
                end = right

            left -= 1
            right += 1

    for i in range(n):
        # Odd length palindrome
        expand(i, i)

        # Even length palindrome
        expand(i, i + 1)

    return [start, end]


print(longestPalindrome("dabac"))    
print(longestPalindrome("cabbad"))   
print(longestPalindrome("xyzzxyxab")) 
print(longestPalindrome("abcd"))     
