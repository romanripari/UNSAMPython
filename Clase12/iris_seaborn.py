# %%
def run():
    from sklearn.datasets import load_iris
    import seaborn as sns
    import pandas as pd

    iris_dataset = load_iris()
    iris_dataframe = pd.DataFrame(iris_dataset['data'], columns = iris_dataset.feature_names)
    iris_dataframe['target'] = iris_dataset['target']

    iris_dataframe['target'].replace([0], 'Setosa', inplace=True)
    iris_dataframe['target'].replace([1], 'Versicolor', inplace=True)
    iris_dataframe['target'].replace([2], 'Virginica', inplace=True)

    sns.pairplot(data = iris_dataframe, hue = 'target', palette='Set1')

    # handles = grafico._legend_data.values()
    # labels = ['setosa', 'versicolor', 'virginica']
    # grafico._legend.remove()
    # grafico.fig.legend(handles=handles, labels=labels, loc='upper center', ncol=3)

if __name__ == '__main__':
    run()