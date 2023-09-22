""" Task 1: Load first a subset of the data to be analyzed """

import re
import pandas as pd

""" Function to read and load csv file to dataframe"""


def import_csv_to_df(csv_file):
    data = []
    flag = 1
    with open(csv_file, "r") as file:
        reader_variable = file.readlines()
        for data_value in reader_variable:
            """ Remove all value from start till , """
            data_value = re.sub(r'^.*?,', '', data_value)
            if flag:
                column_name = (data_value.strip().split(','))
                flag = 0
            else:
                data.append(data_value.strip().split(','))

        df = pd.DataFrame(data, columns=column_name)
    return df


# print(import_csv_to_df('inc_subset.csv'))