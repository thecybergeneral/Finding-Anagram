# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True
string_one = input("Enter first string: ")
string_two = input("Enter second string: ")


def find_anagram(string_one, string_two):
    # [assignment] Add your code here
    if(sorted(string_one) == sorted(string_two)):
        return True
    else:
        return False


print(find_anagram(string_one, string_two))
