"""Data validation with Great Expectations."""

def validate_order_data(df):
    """Validate incoming order data."""
    
    required_cols = [
        'order_id', 'customer_id', 'item_count', 
        'delivery_distance', 'order_value', 'day_of_week',
        'hour_of_day', 'is_weekend', 'courier_experience'
    ]
    
    # Check columns exist
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    
    # Check types
    if (df['item_count'] < 0).any():
        raise ValueError("item_count cannot be negative")
    if (df['delivery_distance'] < 0).any():
        raise ValueError("delivery_distance cannot be negative")
    if (df['order_value'] < 0).any():
        raise ValueError("order_value cannot be negative")
    
    # Check ranges
    if (df['day_of_week'] < 0).any() or (df['day_of_week'] > 6).any():
        raise ValueError("day_of_week must be 0-6")
    if (df['hour_of_day'] < 0).any() or (df['hour_of_day'] > 23).any():
        raise ValueError("hour_of_day must be 0-23")
    
    # Check nulls
    if df.isnull().any().any():
        raise ValueError("Data contains null values")
    
    return True
