import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from Task1 import import_csv_to_df


def main():
    salary_mean = []
    age = []

    extract_df = import_csv_to_df('inc_utf.csv')
    df_test_data = extract_df.sample(frac=0.8)
    df_validation_data = extract_df.sample(frac=0.2)

    # print(extract_df)
    # print(df_test_data)
    # print(df_validation_data)

    df_list = extract_df.groupby('age')['2020'].apply(list).reset_index(name='2020')
    # print(df_list)
    for num in range(df_list.shape[0]):
        salary_mean.append(np.mean(pd.to_numeric(df_list['2020'][num])))
    # print(salary_mean)

    age_list = list(df_list['age'].str.split().str[0])

    for _ in age_list:
        age_string = re.sub('[^a-zA-Z0-9]+', '', _)
        age.append(eval(age_string))
    # print(age)

    age.sort()
    x = np.array(age[:]).reshape((-1, 1))  # extract_df['age'].values.astype(float)
    # x.sort(key=lambda i: i[0])
    # x.sort(key = lambda e: e[0])
    # print(x)
    y = np.array(salary_mean[:]) # extract_df['2020'].values.astype(float)

    # plt.scatter(x, y)
    # plt.show()

    # Transform input data
    poly = PolynomialFeatures(degree=8)
    x_poly = poly.fit_transform(x)

    # Fit the model
    model = LinearRegression()
    model.fit(x_poly, y)

    plt.scatter(x, y)
    plt.plot(x, model.predict(poly.fit_transform(x)), color='r')
    plt.show()


if __name__ == "__main__":
    main()