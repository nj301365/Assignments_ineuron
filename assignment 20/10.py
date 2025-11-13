def is_anagram(s1, s2):
    if sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower()):
        print(f"'{s1}' and '{s2}' are anagrams")
    else:
        print(f"'{s1}' and '{s2}' are not anagrams")

is_anagram("listen", "silent")
is_anagram("hello", "world")
