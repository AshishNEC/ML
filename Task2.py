"""Task2 list to be used"""

import Task1 as t1

grades = [8, 6, 1, 7, 8, 9, 8, 7, 10, 7, 6, 9, 7]


"""Function to evaluate min value without using built in function"""

'''
def customized_min(list_of_grades: list):
    min_value = list_of_grades[0]
    print("in t2")
    for num in list_of_grades:
        if num < min_value:
            min_value = num
    return min_value


"""Function to evaluate max value without using built in function"""


def customized_max(list_of_grades):
    max_value = list_of_grades[0]

    for num in list_of_grades:
        if num > max_value:
            max_value = num
    return max_value


"""Function to evaluate mean value without using built in function"""


def customized_mean(list_of_grades):
    total = 0

    for num in list_of_grades:
        total += num
    return total / len(list_of_grades)


"""Function to evaluate variance and sd without using built in function"""


def customized_variance_and_sd(list_of_grades, mean):
    variance_list = []
    total = 0
    variance_value = 0

    Enable this if required in int
    # mean_value = int(mean)

    for num in list_of_grades:
        Replace mean with mean_value in case in int
    total += ((num - mean) ** 2)

    variance_value = total / len(list_of_grades)

    standard_deviation_value = variance_value ** 0.5
    for num in list_of_grades:
        variance_list.append(num - variance_value)

    return variance_list, standard_deviation_value


"""Function to evaluate median without using built in function"""


def customized_median(grade_list):
    sorted_list = []
    temp_list = list(grade_list)

    while temp_list:
        minimum = temp_list[0]
        for num in temp_list:
            if minimum > num:
                minimum = num
        sorted_list.append(minimum)
        temp_list.remove(minimum)

    sorted_list_length = len(sorted_list)

    if sorted_list_length % 2:
        index_value = int(sorted_list_length / 2 + sorted_list_length % 2)
        return sorted_list[index_value - 1]
    else:
        sub_index_value = int(sorted_list_length / 2)
        return (sorted_list[sub_index_value - 1] + sorted_list[sub_index_value]) / 2


"""Function to evaluate mad without using built in function"""


def customized_median_absolute_deviation(grade_list, orig_median):
    sub_list = []
    sorted_sub_list = []

    for num in grade_list:
        sub_list.append(abs(num - orig_median))

    while sub_list:
        minimum = sub_list[0]
        for x in sub_list:
            if minimum > x:
                minimum = x
        sorted_sub_list.append(minimum)
        sub_list.remove(minimum)

    return customized_median(sorted_sub_list)
'''

"""Calling functions area"""


min_value = t1.customized_min(grades)
print("minimum value is : ", min_value)
max_value = t1.customized_max(grades)
print("maximum value is : ", max_value)
mean = t1.customized_mean(grades)
print("mean value is : ", mean)
variance_list, sd_value = t1.customized_variance_and_sd(grades, mean)
print("variance list is : ", variance_list)
print("sd value is : ", sd_value)
# deviation = customized_standard_deviation(list_of_grades)
median = t1.customized_median(grades)
print("median_value is :", median)
mad = t1.customized_median_absolute_deviation(grades, median)
print("median absolute deviation : ", mad)
