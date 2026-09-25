#!/usr/bin/env python3
"""إنشاء البيانات والنموذج"""

import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from pathlib import Path

data_dir = Path("data/processed")
models_dir = Path("models")
data_dir.mkdir(parents=True, exist_ok=True)
models_dir.mkdir(parents=True, exist_ok=True)

print("=" * 60)
print("🔄 إنشاء البيانات والنموذج")
print("=" * 60)

print("\n📦 إنشاء بيانات تجريبية...")
np.random.seed(42)
n_samples = 1000

data = {
    'customer_id': [f'CUST_{i:04d}' for i in range(n_samples)],
    'order_id': [f'ORD_{i:06d}' for i in range(n_samples)],
    'item_count': np.random.randint(1, 20, n_samples),
    'delivery_distance': np.random.uniform(1, 100, n_samples),
    'order_value': np.random.uniform(10, 500, n_samples),
    'day_of_week': np.random.randint(0, 7, n_samples),
    'hour_of_day': np.random.randint(0, 24, n_samples),
    'is_weekend': np.random.randint(0, 2, n_samples),
    'courier_experience': np.random.uniform(0, 10, n_samples),
    'is_late': np.random.randint(0, 2, n_samples)
}

df = pd.DataFrame(data)

print("✂️ تقسيم البيانات...")
X = df.drop(columns=['order_id', 'customer_id', 'is_late'])
y = df['is_late']

X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

train_df = X_train.copy()
train_df['is_late'] = y_train.values
train_df['order_id'] = df.iloc[X_train.index]['order_id'].values
train_df['customer_id'] = df.iloc[X_train.index]['customer_id'].values

val_df = X_val.copy()
val_df['is_late'] = y_val.values
val_df['order_id'] = df.iloc[X_val.index]['order_id'].values
val_df['customer_id'] = df.iloc[X_val.index]['customer_id'].values

test_df = X_test.copy()
test_df['is_late'] = y_test.values
test_df['order_id'] = df.iloc[X_test.index]['order_id'].values
test_df['customer_id'] = df.iloc[X_test.index]['customer_id'].values

print(f"   Train: {len(train_df)} | Val: {len(val_df)} | Test: {len(test_df)}")

print("\n💾 حفظ البيانات...")
train_df.to_parquet(data_dir / "train_processed.parquet")
val_df.to_parquet(data_dir / "val_processed.parquet")
test_df.to_parquet(data_dir / "test_processed.parquet")
print(f"   ✅ {data_dir}")

print("\n🤖 تدريب النموذج...")
imputer = SimpleImputer(strategy='mean')
scaler = StandardScaler()

X_train_imputed = imputer.fit_transform(X_train)
X_train_scaled = scaler.fit_transform(X_train_imputed)

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=12,
    random_state=42,
    n_jobs=-1
)
model.fit(X_train_scaled, y_train)

X_val_imputed = imputer.transform(X_val)
X_val_scaled = scaler.transform(X_val_imputed)
val_score = roc_auc_score(y_val, model.predict_proba(X_val_scaled)[:, 1])
print(f"   Val ROC-AUC: {val_score:.4f} ✅")

print("\n📦 حفظ النماذج...")
joblib.dump(model, models_dir / "final_model.joblib")
joblib.dump(scaler, models_dir / "scaler.joblib")
joblib.dump(imputer, models_dir / "imputer.joblib")
print(f"   ✅ {models_dir}")

print("\n" + "=" * 60)
print("✅ تم بنجاح!")
print("=" * 60)
