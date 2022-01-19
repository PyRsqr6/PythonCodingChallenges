''' Challenge Statement
Create a function that takes a string as input and returns True only if it contains letters ‘a’ and ‘b’ and all the occurrences of ‘a’ happen before all the occurrences of ‘b’
Length of the string should be 1 - 100000
Eg: 
For string 'aaabbb' - function returns True
For string 'aaabbab' - function returns False
For string 'aaaaa' - function returns True
For string 'bbbb' - function returns True
'''
def string_check(S):
    flag_b = 0
    if len(S) == 0 or len(S) > 100000:
        return False
    for char in S:
        if char != 'a' and char != 'b':
            return False
        if char == 'b':
            flag_b = 1
        if flag_b == 1 and char == 'a':
            return False
    return True

print(" Is 'aaabbb' a valid string ? " + str(string_check('aaabbb')))
print(" Is 'aaabbab' a valid string ? " + str(string_check('aaabbab')))
print(" Is 'aaaaa' a valid string ? " + str(string_check('aaaaa')))
print(" Is 'bbbbb' a valid string ? " + str(string_check('bbbbb')))
print(" Is "" a valid string ? " + str(string_check('')))
print(" Is 'aaabbbj' a valid string ? " + str(string_check('aaabbbj')))