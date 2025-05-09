from sklearn.linear_model import Lasso
import pandas as pd
from sklearn.model_selection import train_test_split
from cross_validate import (
    grid_search
)

def lasso_classifier(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=.8, test_size=.2, random_state=0)
    print('\nTraining Lasso Model\n')
    lasso = Lasso()
    grid = {'alpha':[0.1,1,10]}
    (lasso, _) = grid_search(lasso, grid, X_train, y_train)

    coef = pd.Series(lasso.coef_, index=X.columns)
    print('\nLasso Coef Values: ', coef.sort_values())

    print('\n\nLasso Training R2: ', lasso.score(X_train, y_train))
    print('\nLasso Testing R2: ', lasso.score(X_test, y_test))
    