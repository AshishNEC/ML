import matplotlib.pyplot as plt
import pandas as pd

import Task1 as task1
import Task3 as task3


class Task4:
    def __init__(self):
        self.extract_df = task3.import_csv_to_df()

    def get_number_of_districts(self):
        print("Number of districts : ", self.extract_df.shape[0])

    def get_mean_house_value(self):
        # columns = extract_df[['median_house_value']].mean()
        # print(extract_df['median_house_value'].dtype)
        # df_list = extract_df['median_house_value'].tolist()
        df_list = self.extract_df['median_house_value'].astype(float)
        # print(df_list)
        # df_list = [float(x) for x in df_list]
        # extract_df[['median_house_value']] = pd.to_numeric(extract_df[['median_house_value']])
        # print(extract_df['median_house_value'])
        print(task1.customized_mean(df_list))

    def plot_histogram(self, column_list):
        for column in column_list:
            self.extract_df[column].astype(float).hist(bins=50)
            plt.xlabel(column)
            plt.ylabel('No. of districts')
            plt.title(column + ' Chart')
            plt.show()

    def ocean_proximity_mean(self):
        column_name_list = []
        opm_value_list = []

        df_list = self.extract_df.groupby('ocean_proximity')['median_house_value'].apply(list).reset_index(name='median_house_value')

        for num in range(df_list.shape[0]):
            opm_value_list.append(task1.customized_mean(pd.to_numeric(df_list['median_house_value'][num], downcast='float')))
            column_name_list.append(str(df_list['ocean_proximity'][num]))

        df_opm = pd.DataFrame({
            'Ocean_proximity': column_name_list,
            'Mean Value': opm_value_list
        })
        print(df_opm)


task4_obj = Task4()

""" 4.1: Count the number of districts loaded in this exercise """
task4_obj.get_number_of_districts()

""" 4.2: Calculate the mean of house values among all the districts """
task4_obj.get_mean_house_value()

""" 4.3: Create a histogram for amount_of_households, median_income , housing_median_age and
median_house_value. """
task4_obj.plot_histogram(['households', 'median_income', 'housing_median_age', 'median_house_value'])

""" 4.Additional Task:  For each ocean proximity category in the dataset calculate the mean house value."""
task4_obj.ocean_proximity_mean()



