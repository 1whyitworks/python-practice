# Problem 6: Palindrome Checker (Medium)
# Write a function to check if a given string is a palindrome.
# Ignore case and non-alphanumeric characters.
# Example:
#   Input: "A man, a plan, a canal: Panama"
#   Output: True

import re

def is_palindrome(s):
    # TODO: Clean the string and check if it is a palindrome
    s = re.sub('[^A-Za-z0-9]', '', s).lower()
    return s == s[::-1]
# Test
print(is_palindrome("A man, a plan, a canal: Panama"))  # Expected output: True
