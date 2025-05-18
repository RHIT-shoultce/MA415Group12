from xgboost import XGBClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from cross_validate import (
    grid_search
)

def xgboost_classifier(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=.8, test_size=.2, random_state=0)
    results = pd.DataFrame()

    print('\nTraining XGBoost Classifier Model\n')
    grid = {'max_depth':[20],'n_estimators':[1000], 'learning_rate':[.01, .1]}
    xgbc = XGBClassifier()
    (xgbc, results) = grid_search(xgbc, grid, X_train, y_train)
    
    print('\n\nTraining Accuracy: ', xgbc.score(X_train, y_train))
    print('\nTesting Accuracy: ', xgbc.score(X_test, y_test))

    # ax1 = results.plot.line(x='nehibors', y='train R2')
    # results.plot.line(x='nehibors', y='validation R2', ax=ax1)

    xgbc
