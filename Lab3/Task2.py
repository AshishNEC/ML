import pandas as pd
from Lab2.Task1 import import_csv_to_df
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from yellowbrick.cluster import SilhouetteVisualizer


class Task2:
    def __init__(self):
        self.extract_df = import_csv_to_df('inc_vs_rent.csv')
        self.column_names = list(self.extract_df.columns.values)
        self.dftest = pd.DataFrame(self.extract_df)

    def silhouette_plot(self):
        score_list = []
        k_clusters = [2, 3, 4, 5,6 ,7, 8,9 ,10]
        for i in k_clusters:
            km = KMeans(n_clusters=i, random_state=42, n_init='auto')
            km.fit_predict(self.extract_df[['Annual rent sqm', 'Avg yearly inc KSEK']])
            score = silhouette_score(self.dftest[['Annual rent sqm', 'Avg yearly inc KSEK']], km.labels_, metric='euclidean')
            print('For n_clusters = ', i, ' Silhouette Score: %.3f' % score)
            score_list.append(score)

        plt.plot(k_clusters, score_list)
        plt.xlabel('values of k clusters')
        plt.ylabel('silhouette Score')
        plt.title('Silhouette analysis for optimal k')
        plt.show()

        fig, ax = plt.subplots(2, 2, figsize=(15, 8))
        for i in [2, 3, 4, 5, 6,7 ,8,9,10]:
            km = KMeans(n_clusters=i, init='k-means++', n_init='auto', max_iter=100, random_state=42)
            q, mod = divmod(i, 2)
            visualizer = SilhouetteVisualizer(km, colors='yellowbrick', ax=ax[q - 1][mod])
            visualizer.fit(self.dftest[['Annual rent sqm', 'Avg yearly inc KSEK']])
        visualizer.show()


def main():
    task1_obj = Task2()

    """ 1.1 Load the new dataset """
    # task1_obj.print_df()

    """ 1.2 creating a scatter plot for your points """
    task1_obj.silhouette_plot()


if __name__ == "__main__":
    main()