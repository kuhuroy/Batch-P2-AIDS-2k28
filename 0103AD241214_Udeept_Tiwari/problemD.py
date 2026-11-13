text = input()
palindrome_prefix_length = len(text)

while palindrome_prefix_length > 0:
    prefix = text[:palindrome_prefix_length]
    if prefix == prefix[::-1]:
        break
    palindrome_prefix_length -= 1

print(text[palindrome_prefix_length:][::-1] + text)
