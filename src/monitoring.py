"""Monitoring and metrics tracking."""

import logging
import json
from pathlib import Path
from datetime import datetime

logger = logging.getLogger(__name__)

class PredictionMonitor:
    """Track predictions and metrics."""
    
    def __init__(self, log_file="logs/predictions.log"):
        self.log_file = Path(log_file)
        self.log_file.parent.mkdir(parents=True, exist_ok=True)
        self.request_count = 0
        self.error_count = 0
    
    def log(self, order_id, prediction, probability, latency_ms, status="success"):
        """Log prediction."""
        self.request_count += 1
        if status != "success":
            self.error_count += 1
        
        entry = {
            "timestamp": datetime.now().isoformat(),
            "order_id": order_id,
            "prediction": int(prediction),
            "probability": float(probability),
            "latency_ms": float(latency_ms),
            "status": status
        }
        
        with open(self.log_file, "a") as f:
            f.write(json.dumps(entry) + "\n")
        
        logger.info(f"{order_id} | {status} | {latency_ms:.2f}ms")
    
    def stats(self):
        """Get stats."""
        if self.request_count == 0:
            return {"requests": 0, "errors": 0, "error_rate": 0}
        
        return {
            "requests": self.request_count,
            "errors": self.error_count,
            "error_rate": (self.error_count / self.request_count * 100)
        }

# Global monitor
monitor = PredictionMonitor()
