text = input()
count = 0

for center in range(len(text)):
    left = center - 1
    right = center + 1
    while left >= 0 and right < len(text) and text[left] == text[right]:
        left -= 1
        right += 1
    if right - left - 1 >= 3:
        count += 1

print(count)
