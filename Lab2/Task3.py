import numpy as np
import re
import matplotlib.pyplot as plt
import pandas as pd

from Task1 import import_csv_to_df


def calculate_mse(salary, y_pred):
    number_of_observed_salary = len(salary)
    summation = 0
    for i in range(0,number_of_observed_salary):
        difference = salary[i] - y_pred[i]
        squared_difference = difference**2
        summation = summation + squared_difference
    MSE = summation / number_of_observed_salary
    print("The Mean Square Error is : ", MSE)


class Regression:
    def __init__(self):
        pass

    def find_sum(l, p):
        res = 0

        for i in l:
            res += i ** p

        return res

    def find_mul_sum(l1, l2):
        res = 0

        for i in range(len(l1)):
            res += (l1[i] * l2[i])

        return res

    def solve_equ(sum_x, sum_x2, sum_y, sum_xy, list_len):
        # Equation no 1
        # Ey = a * Ex + b * n

        # Equation no 2
        # Exy = a * Ex^2 + b * Ex

        n = list_len

        p = np.array([[sum_x, n], [sum_x2, sum_x]])
        q = np.array([sum_y, sum_xy])

        res = np.linalg.solve(p, q)

        return res

    def predict(x, res):
        y_pred = []

        for i in x:
            y_pred.append(res[0] * i + res[1])
        return y_pred


def main():
    salary_mean = []
    age = []

    extract_df = import_csv_to_df('inc_utf.csv')
    df_test_data = extract_df.sample(frac=0.8)
    df_validation_data = extract_df.sample(frac=0.2)

    print(extract_df)
    print(df_test_data)
    print(df_validation_data)

    df_list = extract_df.groupby('age')['2020'].apply(list).reset_index(name='2020')
    # print(df_list)
    for num in range(df_list.shape[0]):
        salary_mean.append(np.mean(pd.to_numeric(df_list['2020'][num])))
    #print(salary_mean)

    age_list = list(df_list['age'].str.split().str[0])

    for _ in age_list:
        age_string = re.sub('[^a-zA-Z0-9]+', '', _)
        age.append(eval(age_string))
    #print(age)

    x = age[:] # extract_df['age'].values.astype(float)
    y = salary_mean[:] # extract_df['2020'].values.astype(float)

    r = Regression
    print(x)
    print(y)
    sum_x = r.find_sum(x, 1)
    sum_y = r.find_sum(y, 1)
    sum_x2 = r.find_sum(x, 2)
    sum_xy = r.find_mul_sum(x, y)

    res = []

    res = r.solve_equ(sum_x, sum_x2, sum_y, sum_xy, len(x))

    y_pred = r.predict(x, res)
    # print(y_pred)
    plt.scatter(x, y, color='red')
    plt.plot(x, y_pred, color='blue')
    plt.title('Task2.3')
    plt.xlabel('Age')
    plt.ylabel('Salary 2020')
    plt.show()

    calculate_mse(y, y_pred)
'''
def main():

    #print(extract_df)
    df_list = extract_df.groupby('age')['2020'].apply(list).reset_index(name='2020')
    #print(df_list.shape[0])
    #print(df_list.shape[1])
    #y = extract_df['2020'].values

    print(df_list)
    salary_mean = []
    age_list = []
    for num in range(df_list.shape[0]):
        salary_mean.append(np.mean(pd.to_numeric(df_list['2020'][num])))
        #age_list.append(df_list['age'].str.split().str[0])
    print(salary_mean)
    #age_list.append(df_list['age'].str.split().str[0])
    age_list = list(df_list['age'].str.split().str[0])
    #print(pd.to_numeric(df_list['age'][num]))
    #age_str = df_list['age'].to_list
    #print(type(age_str))
    #print(age_list)
    age = []
    #print ([re.sub('[^a-zA-Z0-9]+', '', _) for _ in my_list])
    for _ in age_list:
        age_string = re.sub('[^a-zA-Z0-9]+', '', _)

        age.append(eval(age_string))
    #age = [eval(i) for i in age_list]
    print(age)

    #age =
    
'''
if __name__ == "__main__":
    main()