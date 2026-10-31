def matches(pattern, word):
    if len(pattern) != len(word):
        return False

    pattern = pattern.lower()
    word = word.lower()

    for p, w in zip(pattern, word):
        if p != '_' and p != w:
            return False

    return True

pattern = input().strip()
dictionary = input().strip().split(':')

result = []

for word in dictionary:
    if matches(pattern, word):
        result.append(word.upper())

if result:
    print(':'.join(result))
else:
    print("ERROR-009")