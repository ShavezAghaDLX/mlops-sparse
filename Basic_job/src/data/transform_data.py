from src.config import config

@config.memory.cache
def transform_data(df):

    return df
