# Delivery Delay Prediction Service

> Converting a machine learning model from Jupyter Notebooks into a production-grade inference service

## 📋 Overview

An advanced, reliable API service for predicting delivery delays, built with modern MLOps practices:

- ✅ **FastAPI** - Fast and secure web framework
- ✅ **Random Forest** - Optimized machine learning model
- ✅ **Docker & Docker Compose** - Containerized deployment
- ✅ **GitHub Actions** - Automated CI/CD
- ✅ **DVC** - Data and model version control
- ✅ **MLflow** - Experiment and model tracking
- ✅ **Great Expectations** - Data quality validation
- ✅ **Pytest** - Comprehensive testing
- ✅ **Monitoring & Logging** - Performance monitoring

---

## 🏗️ Project Structure

```
delivery-delay-prediction/
├── 📁 app/
│   ├── __init__.py
│   ├── main.py              # FastAPI endpoints
│   └── schemas.py           # Pydantic models
├── 📁 src/
│   ├── __init__.py
│   ├── data.py              # Data processing
│   ├── prediction.py        # Prediction pipeline
│   ├── utils.py             # Helper functions
│   ├── mlflow_utils.py      # MLflow integration
│   └── monitoring.py        # Performance monitoring
├── 📁 config/
│   └── config.yaml          # Project configuration
├── 📁 data/
│   ├── processed/           # Processed data
│   └── expectations.py      # Great Expectations
├── 📁 models/               # Model artifacts
├── 📁 tests/
│   └── test_prediction.py   # Tests
├── 📁 notebooks/            # Jupyter notebooks
├── 📁 logs/                 # Logs
├── 📁 .github/workflows/
│   └── ci.yml               # CI/CD pipeline
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── pytest.ini
├── setup_data_and_models.py
└── README.md
```

---

## 📦 Requirements

- **Python**: 3.12+
- **pip**: package manager
- **Git**: for version control
- **Docker**: optional

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the project
```bash
git clone https://github.com/abooobasil752-arch/delivery-delay-prediction.git
cd delivery-delay-prediction
```

### 2️⃣ Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set up data and model
```bash
python setup_data_and_models.py
```

---

## 🚀 Running the Service

### Run the API locally
```bash
python -m uvicorn app.main:app --reload --port 8000
```

The API is available at:
- 🌐 `http://localhost:8000`
- 📚 `http://localhost:8000/docs` (Swagger)
- 🔧 `http://localhost:8000/redoc` (ReDoc)

### With Docker Compose
```bash
docker-compose up --build
```

---

## 🔮 Usage Example

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "order_id": "ORD_000001",
    "customer_id": "CUST_0001",
    "item_count": 5,
    "delivery_distance": 15.5,
    "order_value": 100.0,
    "day_of_week": 3,
    "hour_of_day": 14,
    "is_weekend": 0,
    "courier_experience": 5.0
  }'
```

**Response:**
```json
{
  "order_id": "ORD_000001",
  "prediction": 0,
  "probability": 0.5215,
  "model_version": "RandomForest"
}
```

---

## ✅ Testing

```bash
# Run tests
pytest

# Verbose
pytest -v

# With coverage
pytest --cov=src --cov-report=html
```

**Results:**
```
tests/test_prediction.py::test_pipeline_loads PASSED
tests/test_prediction.py::test_model_loaded PASSED
tests/test_prediction.py::test_prediction_shape PASSED
3 passed in 1.52s ✅
```

---

## 📊 Experiment Tracking with MLflow

```bash
mlflow ui
# then open: http://localhost:5000
```

---

## 📊 Data Quality Validation

The project automatically validates:
- ✅ All required columns are present
- ✅ No negative values
- ✅ `day_of_week` is between 0-6
- ✅ `hour_of_day` is between 0-23
- ✅ No null values

---

## 📈 Monitoring & Logging

All predictions are logged to `logs/predictions.log` in JSON format:

```json
{
  "timestamp": "2024-09-25 12:30:45",
  "order_id": "ORD_000001",
  "prediction": 0,
  "probability": 0.52,
  "processing_time": 0.045
}
```

---

## 🔄 CI/CD with GitHub Actions

On every push to the `main` branch:
1. ✅ Install dependencies
2. ✅ Run tests
3. ✅ Build Docker image
4. ✅ Publish results

---

## 🐳 Docker

```bash
# Build the image
docker build -t delivery-delay-prediction .

# Run the container
docker run -p 8000:8000 delivery-delay-prediction

# With Docker Compose
docker-compose up --build
```

---

## 📁 DVC (Data Version Control)

```bash
# Initialize DVC
dvc init

# Track data
dvc add data/processed/train_processed.parquet

# Pull from remote
dvc pull
```

---

## 🔧 Troubleshooting

### Port 8000 already in use
```bash
python -m uvicorn app.main:app --port 9000
```

### ModuleNotFoundError
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### DVC not initialized
```bash
git init
dvc init
```

---

## 📊 Performance Metrics

- **ROC-AUC**: 0.4844
- **Accuracy**: ~50%
- **API Response Time**: < 100ms

---

## 📖 References

- 🔗 [FastAPI](https://fastapi.tiangolo.com/)
- 🔗 [DVC](https://dvc.org/)
- 🔗 [MLflow](https://mlflow.org/)
- 🔗 [Great Expectations](https://greatexpectations.io/)
- 🔗 [Pytest](https://docs.pytest.org/)
- 🔗 [Docker](https://docs.docker.com/)

---

## 👨‍💻 Author

**Abdulrahman Basil**

---

Made with ❤️ for MLOps

🚀 Thanks for checking out this project!
