---
layout: post
title: Understanding data_ingestion.py
# description: Laying the Foundation Right # Starting an end-to-end machine learning journey, one commit at a time
# thumbnail: /assets/images/ml/e2e-projects/project-1/day-1.png
author: Dipak Pulami Magar
date:   2026-01-27 14:12:45 +0545
categories: ml e2e-project
status: draft
---

## What is `data_ingestion.py`?

`data_ingestion.py` is responsible for  **bringing data into your ML system in a clean, reproducible, and automated way** .

In simple terms:

> It fetches raw data from a source and stores it in a structured format that the rest of the ML pipeline can consume.

This is  **Step 1 of the ML pipeline** :

```
Data Ingestion → Data Validation → Data Transformation → Model Training → Evaluation → Deployment
```

---

## Why do we need a separate `data_ingestion.py`?

In real-world projects, data rarely lives nicely in a CSV file on your laptop.

Data may come from:

* Databases (MySQL, PostgreSQL)
* APIs
* Cloud storage (S3, GCS)
* Data warehouses
* Logs / streaming systems
* Third-party datasets

Having a dedicated ingestion module:

* Makes the pipeline **modular**
* Enables **automation**
* Ensures **reproducibility**
* Helps with **error handling & logging**
* Allows easy switching of data sources

---

## Responsibilities of `data_ingestion.py`

Typically, `data_ingestion.py` does the following:

1. **Read data from source**
   * CSV / Excel
   * Database
   * API
2. **Split data**
   * Train
   * Test (and sometimes validation)
3. **Store artifacts**
   * Save raw data
   * Save train/test datasets
4. **Return paths**
   * So downstream components know where data lives
5. **Log everything**
6. **Handle exceptions cleanly**

---

## Typical Folder Structure

```
project/
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│
├── artifacts/
│   ├── raw_data.csv
│   ├── train.csv
│   ├── test.csv
```

---

## Example: `data_ingestion.py`

Below is a **production-style implementation** used in many real ML projects.

### 1️⃣ Configuration using `dataclass`

```python
from dataclasses import dataclass
import os

@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join("artifacts", "raw_data.csv")
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
```

👉 Why `dataclass`?

* Centralized configuration
* Easy to modify paths
* Clean and readable

---

### 2️⃣ Data Ingestion Class

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from src.logger import logging
from src.exception import CustomException
import sys
import os
```

```python
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
```

---

### 3️⃣ Reading & Saving Data

```python
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method")

        try:
            # Read data
            df = pd.read_csv("data/source_data.csv")
            logging.info("Dataset read successfully")

            # Create artifacts directory
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)

            # Save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Raw data saved")
```

---

### 4️⃣ Train-Test Split

```python
            train_set, test_set = train_test_split(
                df,
                test_size=0.2,
                random_state=42
            )

            train_set.to_csv(self.ingestion_config.train_data_path, index=False)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False)

            logging.info("Train-test split completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
```

---

### 5️⃣ Exception Handling

```python
        except Exception as e:
            logging.error("Error in data ingestion")
            raise CustomException(e, sys)
```

---

## Why is logging critical here?

In production:

* Data size may change
* Schema may break
* Source may go down

Logs help you answer:

* ❓ Was data fetched?
* ❓ How many rows?
* ❓ Did split succeed?
* ❓ Where did it fail?

---

## How `data_ingestion.py` fits in the pipeline

```python
if __name__ == "__main__":
    obj = DataIngestion()
    train_path, test_path = obj.initiate_data_ingestion()
```

Later used by:

* `data_transformation.py`
* `model_trainer.py`

---

## Key Takeaways

* `data_ingestion.py` is the **entry point of data** into the ML system
* Keeps data handling **clean, reproducible, and automated**
* Decouples data source logic from modeling logic
* Makes pipelines **production-ready**

---

If you want, next we can:

* 🔹 Write a **blog-ready version**
* 🔹 Add **database / API ingestion**
* 🔹 Convert this into **ML pipeline diagram**
* 🔹 Add **unit tests for data ingestion**

Just tell me where you want to go next 🚀
