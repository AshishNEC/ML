"""Exercise description"""

""" Error: will return after analyzing 1st character of string """


def any_lowercase1(s):
    for c in s:
        print("c is ", c)
        if c.islower():
            return True
        else:
            return False


""" Error: as it will compute character c not string """


def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


""" Error: as it will check only last character """


def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag


""" No error: as or will compute on 0 and 1 """


def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


""" Error: will check reverse condition and return after 1st capital letter comes """


def any_lowercase5(s):
    for c in s:
        print("char is :", c)
        if not c.islower():
            return 'No'
    return 'Yes'
