# first line: 10
@config.memory.cache
def load_iris_target():
    iris = load_iris(return_X_y=False, as_frame=True)
    df = iris.target
    return df
