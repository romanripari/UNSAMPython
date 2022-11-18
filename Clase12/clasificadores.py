# Lo realicé comentando los resultados con mfares07@gmail.com
from sklearn.datasets import  load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

def evaluaciones(iris_dataset, knn, clf, ranfor, svc):
    '''Recibe 4 clasificadores y con cada uno evalúa la data de iris_dataset,
    devolviendo un score para cada uno. Se evalúa con train_test_split random'''
    X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'])
    knn.fit(X_train, y_train)
    score_knn = knn.score(X_test, y_test)
    clf.fit(X_train, y_train)
    score_clf = clf.score(X_test, y_test)
    ranfor.fit(X_train, y_train)
    score_ranfor = ranfor.score(X_test, y_test)
    svc.fit(X_train, y_train)
    score_svc = svc.score(X_test, y_test)

    return score_knn, score_clf, score_ranfor, score_svc

def experimento(N, iris_dataset, knn, clf, ranfor, svc):
    '''Evalúa N veces con los 4 clasificadores los datos de iris_dataset
    y devuelve un string con el promedio de los N scores de cada clasificador'''
    resultados = []
    for _ in range(N):
        resultados.append(evaluaciones(iris_dataset, knn, clf, ranfor, svc)) 
    prom_knn = sum([knn for knn, clf, ranfor, svc in resultados]) / len(resultados)
    prom_clf = sum([clf for knn, clf, ranfor, svc in resultados]) / len(resultados)
    prom_ranfor = sum([ranfor for knn, clf, ranfor, svc in resultados]) / len(resultados)
    prom_svc  = sum([svc for knn, clf, ranfor, svc in resultados]) / len(resultados)
    return f'{"KNeighbors score: {:.5f}".format(prom_knn)}\n'\
            f'{"DecisionTree score: {:.5f}".format(prom_clf)}\n'\
            f'{"Forest score: {:.5f}".format(prom_ranfor)}\n'\
            f'{"SVC score: {:.5f}".format(prom_svc)}\n'


def run():
    
    # Creo los 4 métodos de clasificación 
    iris_dataset = load_iris()    
    knn = KNeighborsClassifier(n_neighbors = 1)
    clf = DecisionTreeClassifier()
    ranfor = RandomForestClassifier()
    svc = SVC()

    # Imprimo el resultado de experimento
    N = 100
    print(experimento(N, iris_dataset, knn, clf, ranfor, svc))

if __name__ == '__main__': 
    run()