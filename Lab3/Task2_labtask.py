import math

import pandas as pd
from Lab2.Task1 import import_csv_to_df
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import itertools
from statistics import mean
from sklearn.model_selection import ParameterGrid


def distance(p0, p1):
    return (p0[0] - p1[0])**2 + (p0[1] - p1[1])**2


def mean_inter_cluster_distance(list1, list2):
    # for p0, p1 in itertools.combinations(list_obj, 2):
    #    for p0, p1 in itertools.combinations(list_obj, 2):
    inter_distance = []

    for p0 in list1:
        for p1 in list2:
            inter_distance.append(distance(p0, p1))
    print(mean(inter_distance))


def mean_intra_cluster_distance(list_obj):
    intra_distance = []
    total_sum = 0

    if len(list_obj) > 1:
        for p0, p1 in itertools.combinations(list_obj, 2):
            intra_distance.append(distance(p0, p1))
        return mean(intra_distance)
    else:
        for x in list_obj:
            for y  in x:
                total_sum = total_sum + y
            average = total_sum / len(x)
        return average


def mean_intra_cluster_distance_updated(list_obj):
    intra_distance = []
    total_sum = 0
    a_i = []

    if len(list_obj) > 1:
        for p0 in list_obj:
            intra_distance = []
            for p1 in list_obj:
                print("value of p0 :", p0, ' value of p1 :', p1)
                intra_distance.append(distance(p0, p1))
                print('intra_distance : ', intra_distance)
            return a_i.append(sum(intra_distance)/(len(intra_distance)-1))
    else:
        for x in list_obj:
            for y  in x:
                total_sum = total_sum + y
            average = total_sum / len(x)
        #return average
    print('a_i', a_i)

# test_list = [(2,3), (1,1), (5,2), (4,9)]
# mean_intra_cluster_distance_updated(test_list)


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

        km = KMeans(n_clusters=3, n_init='auto')
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

        km = KMeans(n_clusters=3, n_init='auto')
        # print(km)
        y_predicted = km.fit_predict(dftest[['Annual rent sqm', 'Avg yearly inc KSEK']])
        print(y_predicted)
        dftest['cluster'] = y_predicted
        print(dftest)
        print('centroids :', km.cluster_centers_)
        # clustered_df = dftest.groupby('cluster').apply(list)
        clustered_df = dftest.groupby('cluster').apply(lambda x: list(zip(x['Annual rent sqm'], x['Avg yearly inc KSEK']))).reset_index(name='points')
        print(clustered_df)
        print(clustered_df.shape)
        list_mean_intra_cluster = []
        for num in range(clustered_df.shape[0]):
            # print(clustered_df['points'][num])
            list_mean_intra_cluster.append(mean_intra_cluster_distance_updated(clustered_df['points'][num]))
        print("list_mean_intra_cluster : ", list_mean_intra_cluster)

        min_distance_between_centroids = []
        # convert numpy 2d array to tuples of list
        centroids_tuple_list = list(map(tuple, km.cluster_centers_))
        print(centroids_tuple_list)

        # create combinations, required after finding min
        centroid_combinations = list((i, j) for ((i, _), (j, _)) in itertools.combinations(enumerate(centroids_tuple_list), 2))
        print('centroid_combinations : ', centroid_combinations)

        for p0, p1 in itertools.combinations(centroids_tuple_list, 2):
            print("value of p0 :", p0, ' value of p1:', p1)
            min_distance_between_centroids.append(math.sqrt(distance(p0, p1)))
        print("min_distance_between_centroids : ", min_distance_between_centroids)
        var = min_distance_between_centroids.index(min(min_distance_between_centroids))
        print(var)

        send_list = []
        for i, x in enumerate(centroid_combinations):
            if i == var:
                for y in x:
                    print('y :', y)
                    send_list.append(list_mean_intra_cluster[y])
                    # send_list.append(clustered_df['points'][y])
        print(send_list)

        # mean distance between 2 cluster points whose centroid distance is minimum
        # 1st parameter : mean of cluster whose centroid value is minimum from other centroids
        # mean_inter_cluster_distance( send_list[0], send_list[1])
        # mean_intra_cluster_distance_updated()



        # mean_inter_cluster_distance(clustered_df['point'][])

def main():
    task1_obj = Task1()

    """ 1.1 Load the new dataset """
    # task1_obj.print_df()

    """ 1.2 creating a scatter plot for your points """
    task1_obj.create_scatter_plot()


if __name__ == "__main__":
    main()