"""FastAPI app."""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import logging
import yaml
import pandas as pd
from datetime import datetime

from src.prediction import PredictionPipeline
from app.schemas import OrderData, PredictionResponse, HealthResponse, InfoResponse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

with open('config/config.yaml', 'r', encoding='utf-8') as f:
    CONFIG = yaml.safe_load(f)

app = FastAPI(
    title="Order Delivery Prediction",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

pipeline = None

@app.on_event("startup")
async def startup():
    global pipeline
    logger.info("Starting...")
    try:
        pipeline = PredictionPipeline()
        logger.info("✓ Ready")
    except Exception as e:
        logger.error(f"✗ Error: {e}")
        raise

@app.get("/")
async def root():
    return {"message": "Order Delivery Prediction API - Ready"}

@app.get("/health", response_model=HealthResponse)
async def health():
    return HealthResponse(status="ok", version="1.0.0")

@app.get("/info", response_model=InfoResponse)
async def info():
    return InfoResponse(
        model_name=CONFIG['model']['name'],
        model_type=CONFIG['model']['type'],
        model_version="1.0.0"
    )

@app.post("/predict", response_model=PredictionResponse)
async def predict(order: OrderData):
    if pipeline is None:
        raise HTTPException(status_code=503, detail="Pipeline not ready")
    
    try:
        logger.info(f"Prediction for order {order.order_id}")
        
        # تحويل البيانات لـ DataFrame
        df = pd.DataFrame([order.dict()])
        result = pipeline.predict(df)
        
        prediction = result['predictions'][0]
        probability = float(max(result['probabilities'][0]))
        
        return PredictionResponse(
            order_id=order.order_id,
            prediction=int(prediction),
            probability=probability,
            model_version=result['model_version']
        )
    
    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
