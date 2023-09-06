import pandas as pd


def import_csv_to_df():
    data = []
    flag = 1
    with open('./housing.csv', "r") as file:
        reader_variable = file.readlines()
        for data_value in reader_variable:
            if flag:
                column_name = (data_value.strip().split(','))
            else:
                data.append(data_value.strip().split(','))

            df = pd.DataFrame(data, columns=column_name)
            flag = 0
    return df
