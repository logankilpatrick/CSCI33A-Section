import re

#1
def remove_e(st):
    """
    Takes in a string, and returns that string with all 'e's removed
    "Hello, dave" -> "Hllo, dav"
    """
    return re.sub(f"e", "", st)

#2 
def replace_digits(st):
    """
    Takes in string, returns string with all digits switched to (DIGIT)
    "I am 20 years old" -> "I am (DIGIT)(DIGIT) years old"
    """
    return re.sub(r"\d", "(DIGIT)", st)

#3
def keep_e(st):
    """
    Takes in string, returns that string with all letters that
    are not e's changed to (NOT_E).
    "Hello" -> "(NOT_E)e(NOT_E)(NOT_E)(NOT_E)"
    """
    return re.sub(r"[A-D | F-Z | a-d | f-z]", "(NOT_E)", st)

#4
def censor_phone(st):
    """
    Takes in a string, and returns that string with only the last 3
    digits of phone numbers. You can assume all numbers will be in 
    the form (DDD)-DDD-DDDD
    "My number is (670)-867-5309" -> My number is (DDD)-DDD-D309
    """
    return re.sub(r"\(\d\d\d\)-\d\d\d-\d(\d\d\d?)", "(DDD)-DDD-D\\1", st)

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
    one_line = re.sub(r"#(.*?)\n", "(COMMENT)#\\1(COMMENT)\n", st)
    return one_line

#6
def piglatinify(st):
    """
    Takes in a string, and returns the pig-latin translation of
    that string.
    Note: You may assume there will be no punctuation for now
    HINT: You may not end up using regular expressions for this one...

    "hello, connor" -> "ello-hay, onnor-cay
    """
    VOWELS = [letter for letter in "aeiou"]
    CONS = [letter for letter in "qwrtyplkjhgfdszxcvbnm"]

    # Make string lowercase, and return itsself if it is the empty string
    st = st.lower()
    if st == "":
        return ""
    
    # Create a new string to return
    new_st = ""
    
    # Change each word to pig latin
    for word in st.split(" "):
        if word[0] in VOWELS:
            new_st += f"{word}-way "
        elif word[1] in CONS:
            new_st += f"{word[2:]}-{word[0:2]}ay "
        else:
            new_st += f"{word[1:]}-{word[0]}ay "

    # removing trailing space
    new_st = new_st[:-1]

    return new_st

        


