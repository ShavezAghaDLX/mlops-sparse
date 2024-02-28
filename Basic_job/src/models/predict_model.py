from joblib import load

def predict_model(df):

    X = df.drop('target', axis=1)
    print('Loading model')
    model = load('./models/lr_model.pkl')
    y = model.predict(X)
    return y