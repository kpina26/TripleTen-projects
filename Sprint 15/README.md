
# Facial Age Prediction with Deep Learning

## Overview
This project involves the development of a deep learning model for predicting facial age using the **ChaLearn Looking at People** dataset. 
The dataset consists of 7,591 facial images with associated real age labels ranging from 1 to 100 years.

The model uses a **ResNet50** convolutional neural network backbone with **transfer learning** and **data augmentation** to improve generalization.

---

## Dataset
- **Total samples**: 7,591
- **Age range**: 1 to 100 years
- **Mean age**: ~31 years
- **Key characteristics**:
  - Imbalance towards younger individuals (15–40 years old)
  - High visual diversity in facial expressions, lighting, and image quality

The dataset is stored in:
- `/datasets/faces/final_files/` → image files
- `/datasets/faces/labels.csv` → contains `file_name` and `real_age` columns

---

## Project Structure
```
.
├── Sprint_15.ipynb        # EDA and model training
├── Sprint_17.ipynb        # Supporting notebooks
├── README.md              # Project documentation
└── datasets/
    └── faces/
        ├── final_files/   # Facial images
        └── labels.csv     # Metadata
```

---

## Methodology

### 1. **Exploratory Data Analysis (EDA)**
- Inspected dataset shape and sample images
- Visualized age distribution
- Found imbalance towards younger age groups

### 2. **Data Preprocessing**
- Image resizing to 224x224 pixels
- Data augmentation:
  - Horizontal flip
  - Rotation
  - Height/width shift

### 3. **Model Architecture**
- **Base model**: ResNet50 (pre-trained on ImageNet, frozen initial layers)
- **GlobalAveragePooling2D** layer
- **Dense(1)** linear output for regression
- Loss function: **Mean Absolute Error (MAE)**
- Optimizer: **Adam**

### 4. **Training**
- Batch size: 32
- Epochs: 20
- Validation split: 25%

---

## Results
- **Validation MAE**: ~7.65 years
- Model demonstrates good generalization but is affected by dataset imbalance.

---

## Potential Improvements
- Use **more balanced datasets**
- Experiment with **different architectures** (EfficientNet, Vision Transformers)
- Apply **weighted loss functions** to address age group imbalance
- Increase dataset size

---

## Installation
```bash
pip install tensorflow pandas matplotlib
```

---

## How to Run

Install Juypter Notebook

Open Sprint 15.ipynb

Install necessary libaries

---

## Author
Developed as part of a deep learning sprint project for facial age prediction.
