""" Exercise 10.11. Two words are a “reverse pair” if each is the reverse of the other.
    Write a program that finds all the reverse pairs in the word list."""

""" Example list """
list_items = ["top", "pot", "asdf", "fdsa", "LTU", "UTL"]

""" Function to find reverse of string in list """


def check_reverse(original_list):
    temp_list = original_list[:]
    reverse_list = []

    for index in range(len(temp_list)):
        sub_index = index
        while sub_index < len(temp_list)-1:
            # if len(temp_list[index]) != len(temp_list[sub_index+1]):
            #    sub_index += 1
            #    continue
            if temp_list[index] == temp_list[sub_index+1][::-1]:
                reverse_list.append(temp_list[index])
            sub_index += 1
    return reverse_list


print("items having reverse present in list : ", check_reverse(list_items))