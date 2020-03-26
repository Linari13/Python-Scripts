import string

def ispangram(str1, alphabet=string.ascii_lowercase):
	""" check whether a string is pangram or not """
	# Convert all letters in lower case
    str1.lower()

    # delete all letter in string from alphabet
    for char in str1:
        if char in alphabet:
            alphabet=alphabet.replace(char,'')   

    # return true if alphabet empty             
    return alphabet == ''