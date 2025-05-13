from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
from cross_validate import grid_search
import matplotlib as plt
import time


def gradient_boosting_classifier(X, y):

    start_time = time.time()
    print('\nTraining Gradient Boosting Classifier Model\n')
    grid = {'learning_rate':[0.001,0.01, 0.1, 1],'n_estimators':[1000, 2000, 3000],'max_depth':[5,10,15]}
    gbt = GradientBoostingClassifier()

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=.8, test_size=.2, random_state=0)
    results = pd.DataFrame()
    (gbtCV, results) = grid_search(gbt, grid, X_train, y_train)
    
    end_time = time.time()
    print(f"Time taken: {round(end_time-start_time, 1)}")

    print('\n\nTraining R2: ', gbtCV.score(X_train, y_train))
    print('\nTesting R2: ', gbtCV.score(X_test, y_test))

    # ax1 = results.plot.line(x='n_estimators', y='train R2')
    # results.plot.line(x='n_estimators', y='validation R2', ax=ax1)

    plt.show()