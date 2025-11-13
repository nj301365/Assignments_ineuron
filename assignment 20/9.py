import string

def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    if alphabet <= set(s.lower()):
        print("It is a pangram")
    else:
        print("It is not a pangram")

is_pangram("The quick brown fox jumps over the lazy dog")
is_pangram("Hello World")
