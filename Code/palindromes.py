#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    text = [char for char in text.lower() if char.isalnum()]

    return is_palindrome_iterative(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # implement the is_palindrome function iteratively here
    """O(n/2) - searches through half the list and compares both sides to itself. 
        dependent on half of n items in the string"""
    last_i = len(text)-1
    # if len(text) % 2:
    #     return text[:half_i+1][::-1] == text[half_i:]
    # return text[:half_i][::-1] == text[half_i:]
    for i in range(len(text)//2):
        if text[i] == text[last_i]:
            last_i -= 1
        else:
            return False
    return True

def is_palindrome_recursive(text, left=None, right=None):
    # implement the is_palindrome function recursively here
    '''Time complexity: o(n/2) searches through half the list and compares both sides to itself.
        dependent on half of n items in the string'''
    if left is None and right is None:
        left = 0
        right = len(text) - 1

    while left < right:
        if text[left] == text[right]:
            return is_palindrome_recursive(text, left+1, right-1)
        return False
    return True


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()