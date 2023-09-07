""" Exercise 10.7. Write a function called has_duplicates that takes a list and returns True if there is any element
    that appears more than once. It should not modify the original list """


def has_duplicates(investigate_list):
    temp_list = []
    for x in investigate_list:
        if x not in temp_list:
            temp_list.append(x)

    if len(investigate_list) != len(temp_list):
        return 'Yes'
    return 'No'


test_list = [1, 2, 3, 4, 5, 6, 1]
print("Does list contain duplicates: ", has_duplicates(test_list))
