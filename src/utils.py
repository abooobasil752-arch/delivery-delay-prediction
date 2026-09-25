"""Utility functions."""

import logging
import yaml

def setup_logging(config_path: str = "config/config.yaml") -> None:
    """Setup logging from config file."""
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    log_config = config['logging']
    logging.basicConfig(
        level=getattr(logging, log_config['level'].upper(), logging.INFO),
        format=log_config['format']
    )

def load_config(config_path: str = "config/config.yaml") -> dict:
    """Load configuration from YAML."""
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)