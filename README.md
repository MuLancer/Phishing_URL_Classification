# Phishing URL Classification

Machine learning project to classify URLs as phishing or legitimate using URL-based features.

## Project Structure

```
├── data/
│   ├── phishing_urls.csv               # Raw dataset
│   └── processed/
│       ├── cleaned_phishing_urls.csv   # Preprocessed dataset after cleaning and feature engineering
│       ├── train_lin.csv               # Training split for linear models (standardised)
│       ├── test_lin.csv                # Test split for linear models (standardised)
│       ├── train_tree.csv              # Training split for tree-based models (unscaled)
│       └── test_tree.csv               # Test split for tree-based models (unscaled)
├── code/
│   ├── data_collection.py              # Data collection script
│   ├── data_preprocessing.ipynb        # Cleaning and feature engineering
│   ├── EDA.ipynb                       # Exploratory data analysis
│   ├── forward_and_backward_selection.ipynb  # Feature selection
│   ├── ML_models_linear.ipynb          # Logistic regression and linear models
│   ├── ML_models_trees.ipynb           # Decision tree and ensemble tree models
│   └── ML_models_ensemble.ipynb        # Ensemble methods and model comparison
└── plots/
    └── roc_curves_ensemble.png         # ROC curves for ensemble models
```

## Workflow

1. **Data Collection** — `data_collection.py` scrapes/assembles raw URL data into `phishing_urls.csv`
2. **Preprocessing** — `data_preprocessing.ipynb` cleans data and engineers features; outputs `cleaned_phishing_urls.csv` and the train/test splits
3. **EDA** — `EDA.ipynb` explores feature distributions and class balance
4. **Feature Selection** — `forward_and_backward_selection.ipynb` identifies informative features
5. **Modelling** — separate notebooks for linear models, tree-based models, and ensemble methods

## Data Notes

- Linear model splits have standardisation applied; tree-based splits do not.
- Raw data is also kept in `code/phishing_urls.csv` alongside the notebooks for convenience.
