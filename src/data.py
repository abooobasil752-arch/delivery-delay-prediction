"""Data loading module."""

import pandas as pd
import logging
from typing import Tuple
from src.utils import load_config

logger = logging.getLogger(__name__)

def load_training_data() -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Load train, val, test data from Task 2."""
    config = load_config()
    data_config = config['data']
    
    logger.info("Loading training data...")
    train_df = pd.read_parquet(data_config['train_file'])
    logger.info(f"✓ Loaded {len(train_df)} training samples")
    
    logger.info("Loading validation data...")
    val_df = pd.read_parquet(data_config['val_file'])
    logger.info(f"✓ Loaded {len(val_df)} validation samples")
    
    logger.info("Loading test data...")
    test_df = pd.read_parquet(data_config['test_file'])
    logger.info(f"✓ Loaded {len(test_df)} test samples")
    
    return train_df, val_df, test_df

def split_features_target(df: pd.DataFrame, target_column: str = "is_late") -> Tuple[pd.DataFrame, pd.Series]:
    """Split features and target."""
    X = df.drop(columns=[target_column])
    y = df[target_column]
    logger.info(f"Features shape: {X.shape}, Target shape: {y.shape}")
    return X, y