#WAP to find if the character is vowel.

def is_vowel(ch):
    return ch.lower() in {'a', 'e', 'i', 'o', 'u'}

ch = input("enter the character : ")

if ch.isalpha() and len(ch) == 1:
    print("vowel" if is_vowel(ch) else "consonant")

else:
    print("invalid output")    


