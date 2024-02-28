from src.config import config
from src.pipeline.pipeline import run_train_pipeline, run_predict_pipeline

df = run_train_pipeline()
y = run_predict_pipeline()
print(y)













