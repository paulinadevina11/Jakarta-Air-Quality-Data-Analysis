from xgboost import XGBClassifier
from catboost import CatBoostClassifier
from sklearn.linear_model import LogisticRegression, RidgeClassifier, SGDClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

import numpy as np
from sklearn.metrics import f1_score, make_scorer, mean_squared_error, accuracy_score
from sklearn.model_selection import  StratifiedKFold

def neg_rmse(y_true, y_pred):
    return -np.sqrt(mean_squared_error(y_true, y_pred))

CONFIG = {
    'DATAPOINT' : {
        'cuaca-harian': "../../data/cuaca-harian/data_cuaca_jakarta.csv",
        'ISPU': "../../data/ISPU/ISPU_DKI_Gabungan.csv",
        'jumlah-penduduk': "../../data/jumlah-penduduk/data-jumlah-penduduk-provinsi-dki-jakarta-berdasarkan-kelompok-usia-dan-jenis-kelamin-tahun-2013-2021-komponen-data.csv",
        'kualitas-air-sungai': "../../data/kualitas-air-sungai/data-kualitas-air-sungai-komponen-data.csv",
        'libur-nasional': "../../data/libur-nasional/dataset-libur-nasional-dan-weekend.csv",
        'NDVI': "../../data/NDVI/indeks-ndvi-jakarta.csv",
        'main_data': "../../data/main_csv/ISPU_collated_df.csv",
    },

    'MODELS': {
        'XGBoost': XGBClassifier(),
        'CatBoost': CatBoostClassifier(),
        'LogReg': LogisticRegression(),
        'RidgeClas': RidgeClassifier(),
        'SGDClas': SGDClassifier(),
        'SVC': SVC(),
        'RandomForest': RandomForestClassifier(),
        'AdaBoost': AdaBoostClassifier(),
        'Naive_Bayes': GaussianNB(),
        'KNN': KNeighborsClassifier(),
        'MLP': MLPClassifier()
    },

    'PARAMS_GRID': {
        "LogReg": {
            "select_k__k": [10, 20, 30, 40, 50],
            "model__C": np.logspace(-4, 2, 20),
            "model__penalty": ["l2"],
            "model__solver": ["lbfgs"],
            "model__class_weight": [None, "balanced"],
            "model__max_iter": [1000]
            },

        "RidgeClas": {
            "select_k__k": [10, 20, 30, 40, 50],
            "model__alpha": np.logspace(-4, 2, 20),
            "model__class_weight": [None, "balanced"]
            },

        "SGDClas": {
            "select_k__k": [10, 20, 30, 40, 50],
            "model__loss": ["hinge", "log_loss", "modified_huber"],
            "model__alpha": np.logspace(-6, -2, 20),
            "model__penalty": ["l1", "l2", "elasticnet"],
            "model__l1_ratio": np.linspace(0.1, 0.9, 5),
            "model__max_iter": [1000],
            "model__learning_rate": ["optimal", "adaptive"]
            },

        "SVC": {
            "select_k__k": [10, 20, 30, 40, 50],
            "model__C": np.logspace(-3, 2, 20),
            "model__kernel": ["linear", "rbf"],
            "model__gamma": ["scale", "auto"],
            "model__class_weight": [None, "balanced"]
            },

        "KNN": {
            "select_k__k": [10, 20, 30, 40, 50],
            "model__n_neighbors": list(range(3, 31)),
            "model__weights": ["uniform", "distance"],
            "model__metric": ["euclidean", "manhattan", "minkowski"],
            "model__p": [1, 2]
            },

        "MLP": {
            "select_k__k": [10, 20, 30, 40, 50],
            "model__hidden_layer_sizes": [
                (50,), (100,), (200,),
                (50, 50), (100, 50)
            ],
            "model__activation": ["relu", "tanh"],
            "model__alpha": np.logspace(-5, -2, 10),
            "model__learning_rate_init": np.logspace(-4, -2, 10),
            "model__solver": ["adam"],
            "model__max_iter": [500]
            },

        "RandomForest": {
            "select_k__k": [10, 20, 30, 40, 50],
            "model__n_estimators": list(range(100, 801, 100)),
            "model__max_depth": [None] + list(range(5, 31, 5)),
            "model__min_samples_split": [2, 5, 10],
            "model__min_samples_leaf": [1, 2, 4],
            "model__max_features": ["sqrt", "log2", None],
            "model__bootstrap": [True, False]
            },

        "AdaBoost": {
            "select_k__k": [10, 20, 30, 40, 50],
            "model__n_estimators": list(range(50, 801, 50)),
            "model__learning_rate": np.logspace(-3, 0, 10),
            "model__algorithm": ["SAMME", "SAMME.R"]
            },

        "Naive_Bayes": {
            "select_k__k": [10, 20, 30, 40, 50],
            "model__var_smoothing": np.logspace(-12, -7, 20)
            },

        "XGBoost": {
            "select_k__k": [10, 20, 30, 40, 50],
            "model__n_estimators": list(range(100, 801, 100)),
            "model__max_depth": list(range(3, 11)),
            "model__learning_rate": np.logspace(-3, -1, 10),
            "model__subsample": np.linspace(0.6, 1.0, 5),
            "model__colsample_bytree": np.linspace(0.6, 1.0, 5),
            "model__gamma": np.linspace(0, 5, 6),
            "model__min_child_weight": [1, 3, 5]
            },

        "CatBoost": {
            "select_k__k": [10, 20, 30, 40, 50],
            "model__iterations": list(range(300, 1201, 100)),
            "model__depth": list(range(4, 11)),
            "model__learning_rate": np.logspace(-3, -1, 10),
            "model__l2_leaf_reg": np.logspace(-2, 2, 10),
            "model__bagging_temperature": np.linspace(0, 1, 5)
            }
    },

    'SCORER': make_scorer(score_func=f1_score, greater_is_better=True, average='macro'),

    'CV': StratifiedKFold(n_splits=5, shuffle=True, random_state=42),

    'IMPUTER_MODEL': {
        'Linear_Regression': LinearRegression(),
        'RandomForest': RandomForestRegressor(n_estimators=200, random_state=42, n_jobs=-1),
        'XGBoost': XGBRegressor(n_estimators=300, max_depth=6, learning_rate=0.05, subsample=0.8, colsample_bytree=0.8, random_state=42, n_jobs=-1)
    },

    'IMPUTER_CATEGORICAL': {
        'KNN': KNeighborsClassifier(),
        'RandomForest': RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1),
        'XGBoost': XGBClassifier()
    },

    'IMPUTER_SCORER_NUM': make_scorer(score_func=neg_rmse, greater_is_better=True),

    'IMPUTER_SCORER_CAT': make_scorer(score_func=accuracy_score, greater_is_better=True),
}

CONFIG["DATAPOINT"]['main_data'] = "../../data/main_csv/ISPU_collated_df.csv"