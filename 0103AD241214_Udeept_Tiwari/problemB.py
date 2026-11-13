text = input()
start = 0
end = 0

for center in range(len(text)):
    left = center
    right = center
    while left >= 0 and right < len(text) and text[left] == text[right]:
        length = right - left + 1
        best_length = end - start + 1
        if length > best_length or (length == best_length and left < start):
            start = left
            end = right
        left -= 1
        right += 1

    left = center
    right = center + 1
    while left >= 0 and right < len(text) and text[left] == text[right]:
        length = right - left + 1
        best_length = end - start + 1
        if length > best_length or (length == best_length and left < start):
            start = left
            end = right
        left -= 1
        right += 1

print(f"[{start}, {end}]")
