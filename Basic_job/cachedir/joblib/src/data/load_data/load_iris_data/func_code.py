# first line: 4
@config.memory.cache
def load_iris_data():
    iris = load_iris(return_X_y=False, as_frame=True)
    df = iris.data
    return df
