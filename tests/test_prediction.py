"""Tests for prediction."""

import pandas as pd
from src.prediction import PredictionPipeline

def test_pipeline_loads():
    """Test pipeline initialization."""
    pipeline = PredictionPipeline()
    assert pipeline is not None
    assert pipeline.model is not None

def test_model_loaded():
    """Test model is loaded."""
    pipeline = PredictionPipeline()
    assert pipeline.scaler is not None
    assert pipeline.imputer is not None

def test_prediction_shape():
    """Test prediction output."""
    pipeline = PredictionPipeline()
    
    # Create sample data with ALL features
    sample_data = pd.DataFrame({
        'order_id': ['ORD_000001'],
        'customer_id': ['CUST_0001'],
        'item_count': [5],
        'delivery_distance': [15.5],
        'order_value': [100.0],
        'day_of_week': [3],
        'hour_of_day': [14],
        'is_weekend': [0],
        'courier_experience': [5.0]
    })
    
    result = pipeline.predict(sample_data)
    
    assert 'predictions' in result
    assert 'probabilities' in result
    assert len(result['predictions']) == 1
    assert 0 <= result['probabilities'][0][1] <= 1
