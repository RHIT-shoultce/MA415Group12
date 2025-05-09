from sklearn.model_selection import GridSearchCV
import pandas as pd

def grid_search(model, grid, X_train, y_train):
    results = pd.DataFrame()
    gridCV = GridSearchCV(model,param_grid=grid,return_train_score=True, cv=3, n_jobs=-1)
    gridCV.fit(X_train,y_train)

    print(' Optimal Parameters:', gridCV.best_params_)
    print(' Optimal Valid R2 =',gridCV.best_score_)

    results['nehibors'] = grid['n_neighbors']
    results['train R2'] = gridCV.cv_results_['mean_train_score']
    results['validation R2'] = gridCV.cv_results_['mean_test_score']
    
    return (gridCV.best_estimator_, results)

