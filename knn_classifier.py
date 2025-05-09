import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from cross_validate import (
    grid_search
)

def knn_classifier(X, y, n_neighbors=20):
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=.8, test_size=.2, random_state=0)
    results = pd.DataFrame()

    print('\nTraining KNN Model\n')
    grid = {'n_neighbors':range(10,1001, 50)}
    knn = KNeighborsClassifier()
    (knn, results) = grid_search(knn, grid, X_train, y_train)
    
    print('\n\nTraining R2: ', knn.score(X_train, y_train))
    print('\nTesting R2: ', knn.score(X_test, y_test))

    ax1 = results.plot.line(x='nehibors', y='train R2')
    results.plot.line(x='nehibors', y='validation R2', ax=ax1)

    plt.show()