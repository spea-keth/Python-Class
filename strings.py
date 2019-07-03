# A sequence of chars enclosed in '' or ""
name = "Developer"
    # string (developer) assigned to var (name)

# To change a long multiline comment to a string, assign it to var

# strings are arrays in  that
greetings  = "hello world"
print(greetings[-1])
print(greetings[0])
print(greetings[1])
print(greetings[2])

# from 0 to 4 but not inc 4 (zero is optional i.e beginning)
print(greetings[0:4])

# from 6 to end
print(greetings[6:])

print(type(greetings))

#split()
'''
str.split(sep=None, maxsplit=-1)
    Return a list of the words in the string, using sep as the delimiter string. 
    If maxsplit is given, at most maxsplit splits are done (thus, the list will have at most maxsplit+1 elements).
    If maxsplit is not specified or -1, then there is no limit on the number of splits (all possible splits are made).

    If sep is given, consecutive delimiters are not grouped together and are deemed to delimit empty strings (for example, '1,,2'.split(',') returns ['1', '', '2']).
    The sep argument may consist of multiple characters (for example, '1<>2<>3'.split('<>') returns ['1', '2', '3']).
    Splitting an empty string with a specified separator returns [''].

'''
# takes arg
#strip()
'''

str.strip([chars])
    Return a copy of the string with the leading and trailing characters removed.
    The chars argument is a string specifying the set of characters to be removed.
    If omitted or None, the chars argument defaults to removing whitespace.
    The chars argument is not a prefix or suffix; rather, all combinations of its values are stripped.

    str.rstrip([chars])
    Return a copy of the string with trailing characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a suffix; rather, all combinations of its values are stripped:
'''
    # greetings.strip()
    # NOT: split(greetings)

#format()

#1. Change the content of var to uppercase & lower case
# str.lower() OR str.upper()
'''
        str.capitalize()
        Return a copy of the string with its first character capitalized and the rest lowercased.
        
        str.swapcase()
        Return a copy of the string with uppercase characters converted to lowercase and vice versa.
        Note that it is not necessarily true that s.swapcase().swapcase() == s.

    '''
#2. Replace 1st char e.g 'hello world' -> 'jello world'