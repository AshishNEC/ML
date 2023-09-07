""" File to execute task 4 of LAB1 """

import matplotlib.pyplot as plt
import pandas as pd

import Task1 as task1
import Task3 as task3


class Task4:
    def __init__(self):
        self.extract_df = task3.import_csv_to_df()
        self.column_names = list(self.extract_df.columns.values)

    """ Function to get districts in csv """
    def get_number_of_districts(self):
        print(f'Number of districts :', self.extract_df.shape[0])

    """ Function to get house value mean(using customized mean of task1) """
    def get_csv_column_mean(self, analysis_data):
        df_list = self.extract_df[analysis_data].astype(float)
        print(f'Mean of ' + analysis_data + ' :', task1.customized_mean(df_list))

    """ Function to plot histogram """
    def plot_histogram(self, column_list):
        for column in column_list:
            self.extract_df[column].astype(float).hist(bins=50)
            plt.xlabel(column)
            plt.ylabel('No. of districts')
            plt.title(column + ' Chart')
            plt.show()

    """ Function to evaluate ocean proximity mean """
    def ocean_proximity_mean(self, analysis_data1, analysis_data2):
        column_name_list = []
        opm_value_list = []

        df_list = self.extract_df.groupby(analysis_data1)[analysis_data2].apply(list).reset_index(name=analysis_data2)

        for num in range(df_list.shape[0]):
            opm_value_list.append(task1.customized_mean(pd.to_numeric(df_list[analysis_data2][num], downcast='float')))
            column_name_list.append(str(df_list[analysis_data1][num]))

        df_opm = pd.DataFrame({
            'Ocean_proximity': column_name_list,
            'Mean Value': opm_value_list
        })
        print(df_opm)


""" Main Function to be executed """


def main():
    task4_obj = Task4()

    """ 4.1: Count the number of districts loaded in this exercise """
    task4_obj.get_number_of_districts()

    """ 4.2: Calculate the mean of house values among all the districts """
    task4_obj.get_csv_column_mean('median_house_value')

    """ 4.3: Create a histogram for amount_of_households, median_income , housing_median_age and
    median_house_value. """
    task4_obj.plot_histogram(['households', 'median_income', 'housing_median_age', 'median_house_value'])

    """ 4.Additional Task:  For each ocean proximity category in the dataset calculate the mean house value."""
    task4_obj.ocean_proximity_mean('ocean_proximity', 'median_house_value')

    task4_obj.get_column_heading()

if __name__ == "__main__":
    main()

