import numpy as np
import matplotlib.pyplot as plt
from Task1 import import_csv_to_df


def calculate_mse(salary, y_pred):
    number_of_observed_salary = len(salary)
    summation = 0
    for i in range(0, number_of_observed_salary):
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

    extract_df = import_csv_to_df('inc_subset.csv')
    df_validation_data = extract_df.sample(frac=0.8)
    df_test_data = extract_df.sample(frac=0.2)

    print(extract_df.shape[0])
    print(df_test_data.shape[0])
    print(df_validation_data.shape[0])

    x = df_test_data['age'].values.astype(float) #.sample(frac=0.2, random_state=42)
    y = df_test_data['2020'].values.astype(float)
    print(y)
    r = Regression

    sum_x = r.find_sum(x, 1)
    sum_y = r.find_sum(y, 1)
    sum_x2 = r.find_sum(x, 2)
    sum_xy = r.find_mul_sum(x, y)

    res = []

    res = r.solve_equ(sum_x, sum_x2, sum_y, sum_xy, len(x))


    y_pred = r.predict(x, res)
    print(y_pred)
    plt.scatter(x, y, color='red')
    plt.plot(x, y_pred, color='blue')
    plt.title('Task2.2')
    plt.xlabel('Age')
    plt.ylabel('Salary 2020')
    plt.show()

    calculate_mse(y, y_pred)


if __name__ == "__main__":
    main()
