"""Prediction pipeline."""

import joblib
import pandas as pd
import logging
import yaml

logger = logging.getLogger(__name__)

def load_config(config_path: str = "config/config.yaml"):
    """Load config."""
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

class PredictionPipeline:
    """Prediction pipeline."""
    
    def __init__(self):
        """Initialize."""
        self.config = load_config()
        logger.info("Loading artifacts...")
        
        self.model = joblib.load(self.config['artifacts']['model_path'])
        self.scaler = joblib.load(self.config['artifacts']['scaler_path'])
        self.imputer = joblib.load(self.config['artifacts']['imputer_path'])
        
        logger.info("✓ Artifacts loaded")
    
    def preprocess(self, df):
        """Preprocess - remove metadata columns first."""
        # فصل الـ metadata عن الـ features
        metadata = df[['order_id', 'customer_id']].copy()
        features_df = df.drop(columns=['order_id', 'customer_id'])
        
        # Imputation
        features_imputed = pd.DataFrame(
            self.imputer.transform(features_df),
            columns=features_df.columns
        )
        
        # Scaling
        features_scaled = pd.DataFrame(
            self.scaler.transform(features_imputed),
            columns=features_imputed.columns
        )
        
        return features_scaled, metadata
    
    def predict(self, df):
        """Predict."""
        df_processed, metadata = self.preprocess(df)
        predictions = self.model.predict(df_processed)
        probabilities = self.model.predict_proba(df_processed)
        
        return {
            "predictions": predictions.tolist(),
            "probabilities": probabilities.tolist(),
            "model_version": self.config['model']['name'],
            "metadata": metadata.to_dict('records')
        }

def get_pipeline():
    """Get pipeline."""
    return PredictionPipeline()
