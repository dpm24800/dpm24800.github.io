---
layout: post
title: Day 3 of My End-to-End ML Project
description: Where Raw Data Meets Production Pipeline
thumbnail: /assets/images/ml/e2e-projects/project-1/day-3.png
author: Dipak Pulami Magar
date:   2026-01-28 5:12:45 +0545
categories: ml e2e-project
status: draft
---

*No models trained yet. But today, I built the data bloodstream that will feed every future prediction.*

Yesterday I gave my project a nervous system (logging + exceptions). Today I built its **circulatory system**—the components that move raw data through cleaning, transformation, and into model-ready form. Still no algorithms. Still no accuracy metrics. But without this foundation? Any model I train tomorrow would be built on quicksand.

Here's how I engineered two critical pipeline components that separate production ML from notebook experiments.

---

### The Two Pillars of Data Preparation

In an end-to-end ML system, data doesn't magically appear model-ready. It flows through two sequential stages:

| Component | Responsibility | Production Criticality |
|-----------|----------------|------------------------|
| **`data_ingestion.py`** | Raw data → Clean artifacts (train/test splits) | Prevents "data drift" between experiments |
| **`data_transformation.py`** | Raw features → Numerical tensors (with preprocessing pipeline) | Eliminates data leakage; enables inference reproducibility |

Let's dissect each component's architecture and why its design choices matter.

---

### `data_ingestion.py`: The Data Gatekeeper

This component is the **single source of truth** for raw data entry into the system. Its job: *ingest once, split once, artifact forever*.

#### Core Responsibilities

```python
# src/components/data_ingestion.py (annotated highlights)
@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join('artifacts', 'data.csv')
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
```

1. **Immutable artifact storage**: All outputs land in `artifacts/`—a sacred directory never manually edited. Why?
   - Reproducibility: Same raw data → same train/test split across runs
   - Auditability: Trace every experiment back to exact data version
   - CI/CD readiness: Artifacts become inputs for automated training jobs

2. **Real-world data cleaning baked in**:
   ```python
   # Critical fix: Spaces and slashes break downstream pipelines!
   df.columns = df.columns.str.replace(' ', '_', regex=True).str.replace('/', '_', regex=True)
   logging.info(f"Renamed columns: {df.columns.tolist()}")
   ```
   → Spaces in column names (`"math score"`) cause silent failures in scikit-learn pipelines. This proactive sanitization prevents 3 AM debugging sessions.

3. **Train/test split as a *component*, not a script**:
   ```python
   train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
   ```
   → Encapsulating the split inside a class method ensures *every* pipeline run uses identical splitting logic—no more "why did my accuracy change?" mysteries.

#### Why This Beats Notebook-Style Data Loading

| Notebook Approach | Production Component Approach |
|-------------------|-------------------------------|
| `df = pd.read_csv("data.csv")` in cell 3 | `DataIngestion().initiate_data_ingestion()` |
| Manual train/test split in cell 5 | Encapsulated split with fixed random_state |
| Outputs saved ad-hoc | Structured artifacts with versioned paths |
| No logging of data shape/schema | Full audit trail via `logging.info()` |
| **Result**: Fragile, non-reproducible | **Result**: Reproducible, auditable, testable |

> **Key insight**: In production ML, *data versioning* is as critical as *code versioning*. The `artifacts/` directory becomes your data version control system.

---

### `data_transformation.py`: The Feature Alchemist

This component performs the most dangerous operation in ML: **converting raw features into numerical tensors without leaking test data into training**. One mistake here invalidates your entire model evaluation.

#### The Architecture: Defense-in-Depth Against Data Leakage

```python
# src/components/data_transformation.py (critical sections)
def get_data_transformer_object(self):
    numerical_columns = ['writing_score', 'reading_score']
    categorical_features = [
        'gender', 'race_ethnicity', 'parental_level_of_education',
        'lunch', 'test_preparation_course'
    ]
    
    # Numerical pipeline: median imputation → standardization
    num_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])
    
    # Categorical pipeline: mode imputation → OHE → scaling (without centering!)
    cat_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("one_hot_encoder", OneHotEncoder(handle_unknown='ignore', sparse_output=False)),
        ("scaler", StandardScaler(with_mean=False))  # Critical: sparse matrices can't be centered
    ])
    
    # Unified preprocessor: routes columns to correct pipelines
    preprocessor = ColumnTransformer([
        ("num_pipeline", num_pipeline, numerical_columns),
        ("cat_pipeline", cat_pipeline, categorical_features)
    ])
    return preprocessor
```

#### Why This Design Prevents Catastrophic Errors

| Risk | Mitigation in This Implementation |
|------|-----------------------------------|
| **Data leakage** | `fit_transform()` ONLY on train data; `transform()` on test data |
| **Unknown categories at inference** | `handle_unknown='ignore'` in OHE prevents runtime crashes |
| **Sparse matrix scaling errors** | `with_mean=False` for categorical features (sparse matrices can't compute mean) |
| **Silent imputation failures** | Explicit `strategy="median"`/`"most_frequent"` instead of defaults |
| **Pipeline reproducibility loss** | Entire preprocessor saved as `preprocessor.pkl` via `save_object()` |

#### The Golden Rule: Fit on Train, Transform on Test

```python
# CORRECT: Learn statistics from TRAIN only
input_feature_train_arr = preprocessing_obj.fit_transform(input_features_train_df)

# CORRECT: Apply TRAIN-learned rules to TEST
input_feature_test_arr = preprocessing_obj.transform(input_features_test_df)
```

→ If you `fit_transform()` on test data, your model "sees" test set statistics during training. Your reported accuracy becomes **fiction**. This component enforces the boundary.

#### Artifact Preservation: The Inference Lifeline

```python
save_object(
    file_path=self.data_transformation_config.preprocessor_obj_file_path,
    obj=preprocessing_obj  # Contains ALL learned parameters (means, stds, OHE categories)
)
```

→ Without this saved `preprocessor.pkl`, your deployed model would fail on new data. Raw inputs would bypass transformation, causing shape mismatches or nonsensical predictions. This artifact bridges training and inference.

---

### How These Components Fit Into the Larger Pipeline

Today's work completes **Stage 1** of the training pipeline:

```
┌──────────────────────────────────────────────────────────────┐
│                    TRAINING PIPELINE (Stage 1)               │
├──────────────┬───────────────────┬───────────────────────────┤
│  Component   │      Input        │         Output            │
├──────────────┼───────────────────┼───────────────────────────┤
│ DataIngestion│ Raw CSV           │ artifacts/train.csv       │
│              │                   │ artifacts/test.csv        │
├──────────────┼───────────────────┼───────────────────────────┤
│ DataTransform│ train.csv/test.csv│ artifacts/train_arr.npy   │
│              │                   │ artifacts/test_arr.npy    │
│              │                   │ artifacts/preprocessor.pkl│
└──────────────┴───────────────────┴───────────────────────────┘
                              ↓
                    [Tomorrow: ModelTrainer]
```

#### Critical Integration Points

1. **Logger integration**: Every major step logs with timestamps:
   ```
   [2026-01-29 10:23:45] 38 DataIngestion - INFO - Read the dataset as dataframe.
   [2026-01-29 10:23:46] 52 DataIngestion - INFO - Train-test split initiated.
   [2026-01-29 10:24:01] 47 DataTransformation - INFO - Obtaining preprocessing object.
   ```
   → Full observability without `print()` statements polluting production logs.

2. **Exception safety net**: Any failure triggers `CustomException` with precise file/line context:
   ```python
   except Exception as e:
       raise CustomException(e, sys)  # Auto-logs with traceback enrichment
   ```
   → No silent failures. No cryptic `KeyError` without context.

3. **Standalone testability**: Both components include `__main__` blocks for isolated validation:
   ```bash
   python src/components/data_ingestion.py
   → Outputs: "Data ingestion standalone test completed!"
   → Validates artifact creation WITHOUT running full pipeline
   ```

---

### Validation: Proving the Data Bloodstream Flows

Before trusting this with model training, I validated the full data flow:

```bash
# Execute ingestion → transformation chain
python src/components/data_ingestion.py

# Verify artifacts created
ls artifacts/
→ data.csv    train.csv    test.csv    preprocessor.pkl

# Inspect log for validation clues
grep "preprocessing object" logs/*/2026_01_29_*.log
→ "Saved preprocessing object."
→ "Applying preprocessing object on training and testing dataframes."
```

This evidence-based validation prevents the #1 ML project killer: *"It worked yesterday but not today."*

---

### Real-World Lesson: The Column Renaming Fix

During testing, I discovered a silent killer:

```python
# Original column name from dataset:
"math score"  # Contains space!

# Without renaming:
df["math score"] → Works in pandas
But breaks in ColumnTransformer which expects valid Python identifiers
```

My fix:
```python
df.columns = df.columns.str.replace(' ', '_', regex=True).str.replace('/', '_', regex=True)
```

→ **Lesson**: Raw data is *never* pipeline-ready. Production systems must sanitize inputs *at ingestion*, not during transformation. This is why data ingestion is a dedicated component—not a preprocessing step.

---

### Day 3 Checklist Complete

- `data_ingestion.py` implemented with artifact management
- Column sanitization (spaces → underscores) baked into ingestion
- `data_transformation.py` with leakage-proof preprocessing pipelines
- Numerical/categorical feature handling with proper imputation strategies
- Preprocessor saved as `preprocessor.pkl` for inference reproducibility
- Standalone validation tests for both components
- Full integration with Day 2's logging/exception infrastructure
- Artifact directory populated with:
  - `artifacts/data.csv` (raw)
  - `artifacts/train.csv` / `test.csv` (split)
  - `artifacts/preprocessor.pkl` (transformation rules)

---

### Tomorrow's Mission (Day 4): The Brains Arrive

With the data bloodstream flowing, tomorrow I'll build the **model training component**:

1. Implement `utils.py` with:
   - `save_object()`: Generic pickle serializer for artifacts
   - `evaluate_models()`: Cross-validation runner for algorithm selection

2. Implement `model_trainer.py` with:
   - Multiple algorithm training (LinearRegression, RandomForest, XGBoost)
   - Hyperparameter tuning via GridSearchCV
   - Best model selection based on R² score
   - Model artifact saving as `model.pkl`

3. Critical integration: Load `train_arr.npy` from today's transformation → train models → save best performer

The pipeline will finally close the loop: **raw data → features → predictions**.

---

### Why Day 3 > Model Training for Long-Term Success

| Activity | Short-Term "Cost" | Long-Term Impact |
|----------|-------------------|------------------|
| Training first model | "Feels productive" | Model becomes obsolete when data schema changes |
| **Building ingestion/transformation** | "No accuracy metric yet" | **Pipeline survives data schema changes, new features, production deployment** |

The brutal truth: **Models are disposable. Pipelines are permanent.** A well-engineered data preparation layer lets you swap algorithms weekly without touching infrastructure. A fragile notebook-style loader breaks with every CSV format change.

---

*Follow my end-to-end ML journey: [GitHub Repo Link](https://github.com/dpm24800/e2e-ml-project)*  
*Day 3 complete. Data bloodstream flowing. Tomorrow: the brains (model training) arrive.*

---

**Key Takeaways**:
1. Data ingestion isn't "just loading CSVs"—it's the foundation of reproducibility via artifact management
2. Data transformation's #1 job: prevent data leakage through strict fit/transform separation
3. Column sanitization at ingestion prevents silent pipeline failures downstream
4. Saving the preprocessor.pkl is non-negotiable for inference reproducibility
5. **Production ML isn't about algorithms—it's about building data bloodstream that never breaks**

*What's your biggest data preparation horror story? Did a space in a column name ever break your pipeline at 2 AM? Share below!*