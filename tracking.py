import mlflow
import os

MLFLOW_TRACKING_URL = os.getenv('MLFLOW_TRACKING_URL')# 'http://13.74.145.30:5000'  
TENANT = os.getenv('TENANT','local')
RUN_LABEL = os.getenv('GO_PIPELINE_LABEL', '0')
USE_MLFLOW = MLFLOW_TRACKING_URL is not None

class track:
    def __enter__(self):
        if USE_MLFLOW:
            mlflow.set_tracking_uri(uri=MLFLOW_TRACKING_URL)
            mlflow.set_experiment(TENANT)
            mlflow.start_run(run_name=RUN_LABEL)
        return self

    def __exit__(self, type, value, traceback):
        if USE_MLFLOW:
            mlflow.end_run()

    def set_model(self, model):
        if USE_MLFLOW:
            print('logging name',model.name)
            mlflow.log_param('model', model.name)

    def log_params(self, params):
        if USE_MLFLOW:
            for param in params:
                print('logging param',param, params[param])
                mlflow.log_param(param, params[param])

    def log_metrics(self, metrics):
        if USE_MLFLOW:
            for metric in metrics:
                print('metric',metric, metrics[metric])
                mlflow.log_metric(metric, metrics[metric])
