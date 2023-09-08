""" Task 3: Load and inspect the housing data """

import pandas as pd

""" Function to read and load csv file to dataframe"""


def import_csv_to_df(csv_file):
    data = []
    flag = 1
    with open(csv_file, "r") as file:
        reader_variable = file.readlines()
        for data_value in reader_variable:
            if flag:
                column_name = (data_value.strip().split(','))
                flag = 0
            else:
                data.append(data_value.strip().split(','))

        df = pd.DataFrame(data, columns=column_name)
    return df


import_csv_to_df('housing.csv')