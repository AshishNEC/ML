import pandas as pd
from Lab2.Task1 import import_csv_to_df
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import numpy as np


class Task1:
    def __init__(self):
        self.extract_df = import_csv_to_df('inc_vs_rent.csv')
        self.column_names = list(self.extract_df.columns.values)

    def print_df(self):
        print(self.extract_df)

    def create_scatter_plot(self):
        rent = self.extract_df['Annual rent sqm'].values.astype(float)
        salary = self.extract_df['Avg yearly inc KSEK'].values.astype(float)
        plt.scatter(rent, salary, label='data points', color='blue')
        plt.xlabel('Annual rent sqm')
        plt.ylabel('Avg yearly inc KSEK')
        plt.show()

        km = KMeans(n_clusters=3)
        # print(km)
        y_predicted = km.fit_predict(self.extract_df[['Annual rent sqm', 'Avg yearly inc KSEK']])
        self.extract_df['cluster'] = y_predicted
        # print(self.extract_df)

        df0 = self.extract_df[self.extract_df['cluster'] == 0]
        df1 = self.extract_df[self.extract_df['cluster'] == 1]
        df2 = self.extract_df[self.extract_df['cluster'] == 2]

        plt.scatter(df0['Annual rent sqm'], df0['Avg yearly inc KSEK'], color='blue')
        plt.scatter(df1['Annual rent sqm'], df1['Avg yearly inc KSEK'], color='green')
        plt.scatter(df2['Annual rent sqm'], df2['Avg yearly inc KSEK'], color='red')

        plt.xlabel('Annual rent sqm')
        plt.ylabel('Avg yearly inc KSEK')
        plt.show()

        scaler = MinMaxScaler()
        dftest = pd.DataFrame(self.extract_df)
        #print(dftest)

        dftest[['Avg yearly inc KSEK', 'Annual rent sqm']] = scaler.fit_transform(dftest[['Avg yearly inc KSEK', 'Annual rent sqm']])
        # self.extract_df['Avg yearly inc KSEK'] = scaler.transform(self.extract_df['Avg yearly inc KSEK'])

        # print(dftest)
        dftest.drop('region', axis='columns', inplace=True)
        dftest.drop('year', axis='columns', inplace=True)
        print(dftest)

        km = KMeans(n_clusters=3)
        # print(km)
        y_predicted = km.fit_predict(dftest[['Annual rent sqm', 'Avg yearly inc KSEK']])
        # print(y_predicted)
        dftest['cluster'] = y_predicted
        print(dftest)
        print(km.cluster_centers_)

        df0 = dftest[dftest['cluster'] == 0]
        df1 = dftest[dftest['cluster'] == 1]
        df2 = dftest[dftest['cluster'] == 2]

        plt.scatter(df0['Annual rent sqm'], df0['Avg yearly inc KSEK'], color='blue')
        plt.scatter(df1['Annual rent sqm'], df1['Avg yearly inc KSEK'], color='green')
        plt.scatter(df2['Annual rent sqm'], df2['Avg yearly inc KSEK'], color='red')
        plt.scatter(km.cluster_centers_[:,0], km.cluster_centers_[:,1], color='black', marker='*', label='centroid')

        plt.xlabel('Annual rent sqm')
        plt.ylabel('Avg yearly inc KSEK')
        plt.show()

        k_rng = range(1,10)
        sse = []
        for k in k_rng:
            km = KMeans(n_clusters=k, n_init='auto')
            km.fit(dftest[['Annual rent sqm', 'Avg yearly inc KSEK']])
            sse.append(km.inertia_)

        plt.xlabel('k')
        plt.ylabel('sum of squared error')
        plt.plot(k_rng, sse)
        plt.show()
        # print(sse)

        # self.extract_df['cluster'] = y_predicted

        # dfA = self.extract_df['Avg yearly inc KSEK']
        # print(dfA)
        # dfB = self.extract_df['Annual rent sqm']
        # print(dfB)
        # self.extract_df['Avg yearly inc KSEK'] = self.extract_df['Avg yearly inc KSEK'].reshape(-1,1)
        # print(self.extract_df)


def main():
    task1_obj = Task1()

    """ 1.1 Load the new dataset """
    # task1_obj.print_df()

    """ 1.2 creating a scatter plot for your points """
    task1_obj.create_scatter_plot()

    
if __name__ == "__main__":
    main()