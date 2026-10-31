
def countCenters(s):
    count = 0
    n = len(s)

    for i in range(n):
        left = i
        right = i

        # Expand around the center
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1

        # Check if palindrome length is 3 or more
        if right - left - 1 >= 3:
            count += 1

    return count


print(countCenters("abcd"))      
print(countCenters("aba"))       
print(countCenters("ababa"))     
print(countCenters("abcbaxyx"))  
