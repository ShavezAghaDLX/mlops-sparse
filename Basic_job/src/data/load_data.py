from sklearn.datasets import load_iris
from src.config import config

@config.memory.cache
def load_iris_data():
    iris = load_iris(return_X_y=False, as_frame=True)
    df = iris.data
    return df

@config.memory.cache
def load_iris_target():
    iris = load_iris(return_X_y=False, as_frame=True)
    df = iris.target
    return df

def load_data(config):
    df = load_iris_data()
    target = load_iris_target()
    df['target'] = target
    return df