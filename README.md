# Jakarta Air Quality Data Analysis

## 📌 Project Overview

This project focuses on **data engineering and exploratory data analysis (EDA)** of air quality in **Jakarta**, using historical **ISPU (Indeks Standar Pencemar Udara)** data combined with **weather, temporal, and environmental context**. The goal is to demonstrate an **end-to-end data workflow** — from raw data ingestion, cleaning, and merging, to structured EDA and visual insight generation.

This repository is intentionally designed as a **Data Engineering & EDA portfolio project**, not a machine learning competition submission.

---

## 🎯 Objectives

* Build a **clean and reproducible data pipeline** for multi-source environmental data
* Perform **systematic EDA** to understand pollution patterns in Jakarta
* Generate **meaningful visualizations** that support analytical insights
* Provide a **well-structured repository** suitable for professional portfolios

---

## 🗂️ Repository Structure

```
Jakarta-Air-Quality-Data-Analysis/
│
├── data/                    # Raw & processed datasets
│   ├── ISPU/                # Historical ISPU data (2010–2025)
│   ├── cuaca-harian/         # Daily weather observations per station
│   ├── NDVI/                # Vegetation index data
│   ├── libur-nasional/       # National holidays & weekends
│   ├── jumlah-penduduk/      # Population statistics
│   ├── kualitas-air-sungai/  # River water quality (contextual)
│   └── main_csv/             # Final merged & analysis-ready datasets
│
├── src/
│   ├── notebooks/            # Jupyter notebooks for data processing & EDA
│   │   ├── data_viewer.ipynb
│   │   ├── MergeData_ISPU.ipynb
│   │   ├── MergeData_Cuaca.ipynb
│   │   ├── data_collation.ipynb
│   │   ├── new_dataeng.ipynb
│   │   └── EDA.ipynb
│   └── tools/                # Configuration & helper utilities
│       └── CONFIG.py
│
├── Pict/                     # EDA output visualizations
├── documentation/            # Feature & variable documentation
│   └── feature_documentation.md
│
├── .gitignore
└── README.md
```

---

## 🔄 Data Engineering Workflow

1. **Data Ingestion**

   * ISPU data from multiple years and stations
   * Weather data (temperature, humidity, wind, precipitation)
   * Calendar effects (holidays, weekdays/weekends)

2. **Data Cleaning & Standardization**

   * Column normalization across years
   * Timestamp alignment and resampling
   * Handling missing and inconsistent measurements

3. **Data Merging & Feature Preparation**

   * ISPU × Weather × Temporal features
   * Station-level and daily aggregation
   * Output: analysis-ready CSVs in `data/main_csv/`

---

## 📊 Exploratory Data Analysis (EDA)

EDA is conducted in `src/notebooks/EDA.ipynb` and includes:

* Distribution of PM2.5, PM10, SO₂, NO₂, O₃
* ISPU category frequency & transitions
* Seasonal and monthly pollution trends
* Weekday vs weekend pollution patterns
* Weather–pollution relationships (wind, humidity, rainfall)
* Correlation analysis between pollutants and environmental variables

All generated figures are stored in the `Pict/` directory for easy reference.

---

## 🧪 How to Run This Project

### 1️⃣ Environment Setup

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

### 2️⃣ Run Notebooks (Recommended Order)

1. `data_viewer.ipynb`
2. `MergeData_ISPU.ipynb`
3. `MergeData_Cuaca.ipynb`
4. `data_collation.ipynb`
5. `new_dataeng.ipynb`
6. `EDA.ipynb`

---

## 📈 Output

* Cleaned and merged datasets ready for analysis
* High-quality EDA visualizations
* Reproducible notebooks documenting each step

---

## 🧠 Intended Use

This project is suitable for:

* **Data Engineering portfolios**
* **EDA-focused data science showcases**
* Environmental data analysis case studies
* Academic or professional project demonstrations

---

## 🚀 Next Step

Analytical insights derived from this EDA are documented separately in a **dedicated PDF report**, focusing on:

* Air pollution behavior in Jakarta
* Environmental and temporal drivers
* Actionable interpretations

(See accompanying insight report.)

---

## 👤 Author

**Paulina Devina Wijaya**
Computer & Data Science Student
Focus: Data Engineering, Analytics, and Applied AI
