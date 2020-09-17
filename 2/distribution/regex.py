import re
#1
def remove_e(st):
    """
    Takes in a string, and returns that string with all 'e's removed
    "Hello, dave" -> "Hllo, dav"
    """
    return st

#2 
def replace_digits(st):
    """
    Takes in string, returns string with all digits switched to (DIGIT)
    "I am 20 years old" -> "I am (DIGIT)(DIGIT) years old"
    """
    return st

#3
def keep_e(st):
    """
    Takes in string, returns that strings with all letters that
    are not e's changed to (NOT_E).
    "Hello" -> "(NOT_E)e(NOT_E)(NOT_E)(NOT_E)"
    """
    return st

#4
def censor_phone(st):
    """
    Takes in a string, and returns that string with only the last 3
    digits of phone numbers. You can assume all numbers will be in 
    the form (DDD)-DDD-DDDD
    "My number is (670)-867-5309" -> My number is (DDD)-DDD-D309
    """
    return st

#5
def IDE_highlight(st):
    """
    Takes in a Python program string, and returns the program where
    each comment is surrounded by (COMMENT) tags
    Challenge: can you get this to include multi-line comments?
    Challenge: can you get this to detect one or more errors and
    surround them with (ERROR) tags? What types of errors could
    you detect? This is an interesting problem to think about, as
    it is used constantly by our IDEs

    # This is a line of code:
    x = 4

    -> 

    (COMMENT)# This is a line of code:(COMMENT)
    x = 4

    Note: auto-tests only work for single-line comments
    """
    return st

#6
def piglatinify(st):
    """
    Takes in a string, and returns the pig-latin translation of
    that string.
    HINT: You may not end up using regular expressions for this one...

    "hello, connor" -> "ello-hay, onnor-cay
    """
    return st


