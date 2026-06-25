# AnomX — Synthetic Forex Behaviour & Anomaly Detection (Midterm Submission)

AnomX is a synthetic data generation and feature engineering project focused on simulating forex trading behaviour for anomaly detection. It builds an end-to-end pipeline that generates user activity, injects anomalous behaviour patterns, and extracts structured features for analysis.

This submission covers work completed from **Week 1 to Week 4**, including Python/Git foundations, event simulation, and feature engineering with exploratory analysis.

---

## Table of Contents
- Week 1–2: Python, Git & Core Concepts
- Week 3: Synthetic Event Generation
- Week 4: Feature Engineering & EDA
- Repository Contents

---

# Week 1–2: Python, Git & Core Concepts

## Python fundamentals
During the initial phase, the focus was on building core Python skills required for data pipeline development:

- functions, classes, and modular code structure
- list/dictionary comprehensions for efficient data handling
- working with datetime for time-based event simulation
- reproducible randomness using seeded generators
- organizing code into multiple files instead of single scripts

## Pandas and NumPy usage
Basic data handling skills were developed using Pandas and NumPy:

- creating and manipulating tabular datasets
- filtering, grouping, and aggregating data
- using vectorized operations instead of loops for efficiency
- handling missing or inconsistent values
- exporting and reloading structured datasets

## Git & GitHub workflow
Version control practices were established to manage project development:

- staged commits aligned with development milestones
- meaningful commit messages reflecting feature progress
- branching for experimentation before merging stable code

## Understanding anomaly detection
Anomaly detection refers to identifying behaviour that deviates significantly from normal patterns within a dataset.

In this project context, anomalies represent:
- unusual trading spikes
- abnormal login patterns
- irregular deposit and withdrawal behaviour

A key challenge is that “normal behaviour” is not fixed and must be learned from the data itself rather than predefined rules.

---

# Week 3: Synthetic Event Generation

## Event simulation system
A synthetic user base is generated where each user is assigned a behavioural profile defining how they typically interact with the system over time.

The system generates a time-ordered stream of events based on these profiles.

## Normal behaviour
Normal users follow consistent behavioural distributions such as:
- stable login frequency
- predictable trade sizes
- regular deposit/withdrawal patterns
- steady session activity over time

## Anomaly injection
A subset of users is intentionally modified to introduce abnormal behavioural patterns.

These anomalies are structured rather than random and are designed to resemble realistic suspicious behaviour.

Examples include:
- sudden spikes in trading activity
- repeated logins from different IPs or regions in short time intervals
- rapid deposit followed by withdrawal with minimal trading activity
- bursts of unusually high activity in short time windows

The goal is to ensure anomalies appear as behavioural patterns rather than isolated outliers.

---

## Event types generated
The synthetic system simulates multiple types of forex platform activity:

- **Logins** → session access, IP, region
- **Trades** → currency pair, trade size, leverage, profit/loss
- **Deposits** → account funding events
- **Withdrawals** → fund removal events
- **Account updates** → profile or configuration changes

Each event is associated with a user and timestamped to preserve sequential behaviour.

---

## Key insights from data generation

- user activity varies significantly even among normal users
- raw event counts alone are not sufficient to detect anomalies
- relative deviations from user behaviour are more meaningful than absolute thresholds
- injecting anomalies as behavioural patterns makes the dataset more realistic and useful for detection tasks

---

# Week 4: Feature Engineering & EDA

## Feature engineering approach
Raw event logs are transformed into structured user-level features. Instead of analyzing events individually, the focus shifts to aggregated behavioural patterns.

Each user is represented using a feature vector summarizing their activity across time.

---

## Feature categories

### 1. Login behaviour features
These capture how users access the system:

- login frequency over time
- number of unique IP addresses
- number of regions accessed
- average time between consecutive logins
- detection of rapid or automated login patterns

---

### 2. Trading behaviour features
These describe financial activity patterns:

- trade frequency per time period
- burst activity in short intervals
- variability in trade sizes
- profit/loss consistency across trades

---

### 3. Deposit and withdrawal behaviour
These capture financial flow patterns:

- ratio of withdrawals to deposits
- frequency of fund movements
- imbalance between deposits and trading activity

---

### 4. Temporal behaviour features
These represent time-based patterns:

- inactivity gaps between events
- time since last transaction or login
- changes in activity intensity over time

---

### 5. Deviation-based features
These measure how much a user deviates from their own historical behaviour:

- z-score style anomaly indicators
- deviation from rolling averages
- sudden spikes relative to baseline activity

---

## Exploratory Data Analysis (EDA)

Before finalizing the feature set, exploratory analysis was performed to validate patterns and ensure anomaly separability.

The analysis included:
- distribution checks for all engineered features
- correlation analysis between related variables
- comparison of normal vs anomalous user behaviour
- validation that injected anomalies are reflected in feature space

---

## Key observations

- raw counts are highly skewed and require normalization
- anomalies are more visible when combining multiple features rather than using single metrics
- temporal and burst-based features are among the strongest behavioural signals
- separating feature engineering from data generation improves modularity and reusability

---

# Repository contents

The repository includes the following components:

- `README.md` → project documentation and submission summary
- `SRC/data_generator.py` → synthetic event generation logic
- `SRC/feature_engineering.py` → feature extraction pipeline
- `data/` → generated synthetic datasets
