"""MLflow for experiment tracking."""

import mlflow
import logging
import os

logger = logging.getLogger(__name__)

def init_mlflow(experiment_name="order-delivery"):
    """Initialize MLflow."""
    mlflow.set_experiment(experiment_name)
    logger.info(f"MLflow initialized: {experiment_name}")

def log_prediction_run(order_id, prediction, probability, latency_ms):
    """Log a prediction run."""
    try:
        with mlflow.start_run():
            mlflow.log_param("order_id", order_id)
            mlflow.log_metric("prediction", prediction)
            mlflow.log_metric("probability", probability)
            mlflow.log_metric("latency_ms", latency_ms)
            logger.debug(f"Logged run for {order_id}")
    except Exception as e:
        logger.warning(f"MLflow logging failed: {e}")

# Initialize on import
try:
    init_mlflow()
except:
    logger.warning("MLflow not available")
