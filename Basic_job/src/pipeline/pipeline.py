from joblib import memory
from src.config import config
from src.data.load_data import load_data
from src.data.transform_data import transform_data
from src.models.train_model import train_model
from src.models.predict_model import predict_model



def run_preprocessing():
    df = load_data(config.pipeline_config)
    df = transform_data(df)
    return df

def run_train_pipeline():
    # task = Task.init(project_name='24-01_clearml_poc', task_name='Train Pipeline')
    df = run_preprocessing()
    train_model(df)
    # task.close()
    return df

def run_predict_pipeline():
    df = run_preprocessing()
    y = predict_model(df)
    return df
