# MLOps Task 3: Production Inference Service

> تحويل نماذج التعلم الآلي من Jupyter Notebooks إلى خدمة إنتاجية احترافية

## 📋 نظرة عامة

خدمة API متقدمة وموثوقة للتنبؤ بتأخر التسليمات باستخدام أحدث تقنيات MLOps:

- ✅ **FastAPI** - Web Framework سريع وآمن
- ✅ **Random Forest** - نموذج تعلم آلي محسّن
- ✅ **Docker & Docker Compose** - حاويات للتوزيع
- ✅ **GitHub Actions** - CI/CD مؤتمت
- ✅ **DVC** - إدارة البيانات والنماذج
- ✅ **MLflow** - تتبع التجارب والنماذج
- ✅ **Great Expectations** - التحقق من جودة البيانات
- ✅ **Pytest** - اختبارات شاملة
- ✅ **Monitoring & Logging** - مراقبة الأداء

---

## 🏗️ هيكل المشروع

```
mlops-task3-delivery/
├── 📁 app/
│   ├── __init__.py
│   ├── main.py              # FastAPI endpoints
│   └── schemas.py           # Pydantic models
├── 📁 src/
│   ├── __init__.py
│   ├── data.py              # معالجة البيانات
│   ├── prediction.py        # Pipeline التنبؤ
│   ├── utils.py             # دوال مساعدة
│   ├── mlflow_utils.py      # تكامل MLflow
│   └── monitoring.py        # مراقبة الأداء
├── 📁 config/
│   └── config.yaml          # إعدادات المشروع
├── 📁 data/
│   ├── processed/           # بيانات معالجة
│   └── expectations.py      # Great Expectations
├── 📁 models/               # ملفات النموذج
├── 📁 tests/
│   └── test_prediction.py   # اختبارات
├── 📁 notebooks/            # Jupyter notebooks
├── 📁 logs/                 # السجلات
├── 📁 .github/workflows/
│   └── ci.yml               # CI/CD Pipeline
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── pytest.ini
├── setup_data_and_models.py
└── README.md
```

---

## 📦 المتطلبات

- **Python**: 3.12+
- **pip**: مدير الحزم
- **Git**: للـ Version Control
- **Docker**: اختياري

---

## ⚙️ الإعداد والتثبيت

### 1️⃣ استنساخ المشروع
```bash
git clone https://github.com/abooobasil752-arch/mlops-task3-delivery.git
cd mlops-task3-delivery
```

### 2️⃣ إنشاء Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# أو
venv\Scripts\activate  # Windows
```

### 3️⃣ تثبيت المكتبات
```bash
pip install -r requirements.txt
```

### 4️⃣ إعداد البيانات والنموذج
```bash
python setup_data_and_models.py
```

---

## 🚀 التشغيل

### تشغيل API محلياً
```bash
python -m uvicorn app.main:app --reload --port 8000
```

الـ API متاح على:
- 🌐 `http://localhost:8000`
- 📚 `http://localhost:8000/docs` (Swagger)
- 🔧 `http://localhost:8000/redoc` (ReDoc)

### مع Docker Compose
```bash
docker-compose up --build
```

---

## 🔮 مثال الاستخدام

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

**الرد:**
```json
{
  "order_id": "ORD_000001",
  "prediction": 0,
  "probability": 0.5215,
  "model_version": "RandomForest"
}
```

---

## ✅ الاختبارات

```bash
# تشغيل الاختبارات
pytest

# مع تفاصيل
pytest -v

# مع تغطية
pytest --cov=src --cov-report=html
```

**النتائج:**
```
tests/test_prediction.py::test_pipeline_loads PASSED
tests/test_prediction.py::test_model_loaded PASSED
tests/test_prediction.py::test_prediction_shape PASSED
3 passed in 1.52s ✅
```

---

## 📊 تتبع التجارب مع MLflow

```bash
mlflow ui
# ثم افتح: http://localhost:5000
```

---

## 📊 التحقق من جودة البيانات

المشروع يتحقق تلقائياً من:
- ✅ وجود جميع الأعمدة المطلوبة
- ✅ عدم وجود قيم سالبة
- ✅ `day_of_week` بين 0-6
- ✅ `hour_of_day` بين 0-23
- ✅ عدم وجود null values

---

## 📈 المراقبة والتسجيل

جميع التنبؤات تُسجل في `logs/predictions.log` بصيغة JSON:

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

## 🔄 CI/CD مع GitHub Actions

عند كل push للـ `main` branch:
1. ✅ تثبيت المكتبات
2. ✅ تشغيل الاختبارات
3. ✅ بناء صورة Docker
4. ✅ نشر النتائج

---

## 🐳 Docker

```bash
# بناء الصورة
docker build -t mlops-task3 .

# تشغيل الحاوية
docker run -p 8000:8000 mlops-task3

# مع Docker Compose
docker-compose up --build
```

---

## 📁 DVC (Data Version Control)

```bash
# تهيئة DVC
dvc init

# تتبع البيانات
dvc add data/processed/train_processed.parquet

# السحب من النسخة السابقة
dvc pull
```

---

## 🔧 معالجة الأخطاء الشائعة

### Port 8000 مشغول
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

## 📊 مقاييس الأداء

- **ROC-AUC**: 0.4844
- **Accuracy**: ~50%
- **API Response Time**: < 100ms

---

## 📖 المراجع

- 🔗 [FastAPI](https://fastapi.tiangolo.com/)
- 🔗 [DVC](https://dvc.org/)
- 🔗 [MLflow](https://mlflow.org/)
- 🔗 [Great Expectations](https://greatexpectations.io/)
- 🔗 [Pytest](https://docs.pytest.org/)
- 🔗 [Docker](https://docs.docker.com/)

---

## 👨‍💻 المؤلف

**abalrahman**

---

## 📅 معلومات المشروع

- **المقرر**: MLOps Training 2026/2027
- **المهمة**: Task 3 - Production Inference Service
- **التاريخ**: September 2026
- **الحالة**: ✅ مكتمل

---

Made with ❤️ for MLOps Training

🚀 شكراً لاستخدام هذا المشروع!
