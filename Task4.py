""" File to execute task 4 of LAB1 """

import matplotlib.pyplot as plt
import pandas as pd

import Task1 as task1
import Task3 as task3


class Task4:
    def __init__(self):
        self.extract_df = task3.import_csv_to_df('housing.csv')
        self.column_names = list(self.extract_df.columns.values)

    """ Function to validate column name """

    def validate_column(self, column_name):
        if column_name not in self.column_names:
            return False
        return True

    """ Function to get districts in csv """

    def get_number_of_districts(self):
        print(f'Number of districts :', self.extract_df.shape[0])

    """ Function to get mean of any csv column (using customized mean of task1) """

    def get_csv_column_mean(self, analyze_data_column):
        if not self.validate_column(analyze_data_column):
            print("invalid column ", analyze_data_column)
            return False
        df_list = self.extract_df[analyze_data_column].astype(float)
        print(f'Mean of ' + analyze_data_column + ' :', task1.customized_mean(df_list))

    """ Function to plot histogram """

    def plot_histogram(self, column_list):
        for column in column_list:
            self.extract_df[column].astype(float).hist(bins=50)
            plt.xlabel(column)
            plt.ylabel('No. of districts')
            plt.title(column + ' Chart')
            plt.show()

    """ Function to evaluate ocean proximity mean """

    def ocean_proximity_mean(self, analyze_data_column1, analyze_data_column2):
        column_name_list = []
        opm_value_list = []

        df_list = self.extract_df.groupby(analyze_data_column1)[analyze_data_column2].apply(list).reset_index(name=analyze_data_column2)

        for num in range(df_list.shape[0]):
            opm_value_list.append(task1.customized_mean(pd.to_numeric(df_list[analyze_data_column2][num], downcast='float')))
            column_name_list.append(str(df_list[analyze_data_column1][num]))

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


if __name__ == "__main__":
    main()
