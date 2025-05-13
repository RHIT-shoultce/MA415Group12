from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from cross_validate import (
    grid_search
)

def random_forest_classifier(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=.8, test_size=.2, random_state=0)
    results = pd.DataFrame()

    print('\nTraining Random Forest Classifier Model\n')
    grid = {'max_depth':[1,2,3,10,20],'n_estimators':[1000, 2000, 4000]}
    rfc = RandomForestClassifier()
    (rfc, results) = grid_search(rfc, grid, X_train, y_train)
    
    print('\n\nTraining Accuracy: ', rfc.score(X_train, y_train))
    print('\nTesting Accuracy: ', rfc.score(X_test, y_test))

    # ax1 = results.plot.line(x='nehibors', y='train R2')
    # results.plot.line(x='nehibors', y='validation R2', ax=ax1)

    rfc

