from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from joblib import dump

def train_model(df):

    X = df.drop('target', axis=1)
    y = df['target']

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X, y)
    score = cross_val_score(model, X, y, cv=5, scoring='accuracy', n_jobs=-2).mean()
    print(f"Cross validation score: {score}")
    model.fit(X, y)
    
    print('Saving model')
    dump(model, './models/lr_model.pkl')

    return model