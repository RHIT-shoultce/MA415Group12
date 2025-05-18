import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA

def pca(X, y, n_components=0.9):
    # Split the dataset into training and test sets

    # Perform PCA
    print('\nApplying PCA...')
    pca = PCA(n_components=n_components)  # You can set n_components to an integer or a percentage
    X_PCA = pca.fit_transform(X)  # Fit and transform training data

    print(f"Explained variance ratio: {pca.explained_variance_ratio_}")
    print(f"Number of components after PCA: {X_PCA.shape[1]}")
    
    components = pd.DataFrame(pca.components_, columns=X.columns)
    print(components)

    return X_PCA