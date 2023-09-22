""" Exercise 11.4. If you did Exercise 10.7, you already have a function named
    has_duplicates that takes a list as a parameter and returns True if there
    is any object that appears more than once in the list. Use a dictionary to write
    a faster, simpler version of has_duplicates."""


dict_value = {"a": 1, "b": 2, "c": 3, "d": 3}


def has_duplicates(test_dict):
    uniques = {}

    for key, value in test_dict.items():
        if value not in uniques.values():
            uniques.update({key: value})
        else:
            return 'Yes'
    return 'No'


print("Does dict has duplicates : ", has_duplicates(dict_value))

