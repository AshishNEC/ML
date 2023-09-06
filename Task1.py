"""Random list to be used"""
list_of_grades = [8, 6, 1, 7, 18, 9, 28, 17, 100, 27, 36, 19, 77, 89]

"""Function to evaluate min value without using built in function"""


def customized_min(grade_list: list):
    min_value = grade_list[0]

    for num in grade_list:
        if num < min_value:
            min_value = num
    return min_value


"""Function to evaluate max value without using built in function"""


def customized_max(grade_list):
    max_value = grade_list[0]

    for num in grade_list:
        if num > max_value:
            max_value = num
    return max_value


"""Function to evaluate mean value without using built in function"""


def customized_mean(grade_list):
    total = 0

    for num in grade_list:
        total += num
    return total / len(grade_list)


"""Function to evaluate variance and sd without using built in function"""


def customized_variance_and_sd(grade_list, mean):
    variance_list = []
    total = 0
    variance_value = 0

    '''Enable this if required in int'''
    # mean_value = int(mean)

    for num in grade_list:
        '''Replace mean with mean_value in case in int'''
        total += ((num - mean) ** 2)

    variance_value = total / len(grade_list)

    standard_deviation_value = variance_value ** 0.5
    for num in grade_list:
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


"""Calling functions area"""

'''
min_value = customized_min(list_of_grades)
print("minimum value is : ", min_value)
max_value = customized_max(list_of_grades)
print("maximum value is : ", max_value)
mean = customized_mean(list_of_grades)
print("mean value is : ", mean)
variance_list, sd_value = customized_variance_and_sd(list_of_grades, mean)
print("variance list is : ", variance_list)
print("sd value is : ", sd_value)
# deviation = customized_standard_deviation(list_of_grades)
median = customized_median(list_of_grades)
print("median_value is :", median)
mad = customized_median_absolute_deviation(list_of_grades, median)
print("median absolute deviation : ", mad)
'''