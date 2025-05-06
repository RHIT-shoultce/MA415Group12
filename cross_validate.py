from sklearn.model_selection import GridSearchCV

def grid_search(model, grid, X_train, y_train):
    gridCV = GridSearchCV(model,param_grid=grid,return_train_score=True, cv=3, n_jobs=-1)
    gridCV.fit(X_train,y_train)

    print(' Optimal Parameters:', gridCV.best_params_)
    print(' Optimal Valid R2 =',gridCV.best_score_)
    
    return gridCV.best_estimator_

