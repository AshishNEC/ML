"""
Exercise 14.1. Write a function called sed that takes as arguments a pattern string, a replacement string,
and two filenames; it should read the first file and write the contents into the second file (creating it if necessary).
If the pattern string appears anywhere in the file, it should be replaced with the replacement string
"""

import re


def sed(pattern_string, replacement_string, file1, file2):
    try:
        fp1 = open(file1, 'r')
        fp2 = open(file2, 'w')

        for line in fp1:
            line = re.sub(pattern_string, replacement_string, line, flags=re.IGNORECASE)
            fp2.write(line)
    except:
        print('file :', file1, 'does not exist')


sed('This', 'that', 'input1.txt', 'output.txt')
