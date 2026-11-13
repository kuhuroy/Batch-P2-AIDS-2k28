text = input()
count = 0

for center in range(len(text)):
    left = center
    right = center
    while left >= 0 and right < len(text) and text[left] == text[right]:
        count += 1
        left -= 1
        right += 1

    left = center
    right = center + 1
    while left >= 0 and right < len(text) and text[left] == text[right]:
        count += 1
        left -= 1
        right += 1

print(count)