
def countSubstrings(s):
    count = 0
    n = len(s)

    def expand(left, right):
        nonlocal count

        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

    for i in range(n):
        # Odd length palindromes
        expand(i, i)

        # Even length palindromes
        expand(i, i + 1)

    return count


print(countSubstrings("abc"))   
print(countSubstrings("aba"))   
print(countSubstrings("abba"))  
print(countSubstrings("aaa"))   
print(countSubstrings("xabay")) 
print(countSubstrings("racecar")) 