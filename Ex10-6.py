"""Exercise 10.6. Two words are anagrams if you can rearrange the letters from one to spell the other. Write a function
called is_anagram that takes two strings and returns True if they are anagrams."""

"""Function to check formation of 1 string from another"""


def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return 'No'
    for x in str1:
        if x not in str2:
            return 'No'
    return 'Yes'


print("Are strings anagram : ", is_anagram('topd', 'pdto'))