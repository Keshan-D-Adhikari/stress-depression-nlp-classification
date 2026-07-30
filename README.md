# Stress vs Depression NLP Classification

## Project Overview
This project investigates the classification of Reddit posts into two categories: Stress and Depression.

The study compares traditional machine-learning approaches with a transformer-based NLP model under the same experimental conditions.

## Dataset
Two Reddit-derived datasets are used:

- Dreaddit dataset for Stress samples
- Depression Reddit Cleaned Dataset for Depression samples

After preprocessing, duplicate removal, and class balancing, the final dataset contains:

- Stress: 1,854 samples
- Depression: 1,854 samples
- Total: 3,708 samples

## Models
The following models will be compared:

1. TF-IDF + Logistic Regression
2. TF-IDF + Support Vector Machine (SVM)
3. BERT

## Evaluation
The models will be evaluated using:

- Macro-F1 Score
- Precision
- Recall
- Accuracy
- Confusion Matrix

## Current Progress
- [x] Dataset collection
- [x] Data preprocessing
- [x] Duplicate removal
- [x] Class balancing
- [x] Text-length analysis
- [ ] Logistic Regression training
- [ ] SVM training
- [ ] BERT fine-tuning
- [ ] Model evaluation

## Ethical Considerations
The project uses existing Reddit-derived datasets for research purposes. Model outputs are treated only as experimental text classifications and are not intended to represent clinical diagnoses or treatment recommendations.
