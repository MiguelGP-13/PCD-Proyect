# Proyecto: Clasificación e Interpretabilidad de Lesiones Cutáneas con HAM10000

## Descripción

Este proyecto utiliza el dataset [**HAM10000**](https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000), que contiene imágenes dermatoscópicas de siete tipos de lesiones cutáneas. El objetivo es construir un pipeline jerárquico que permita:

1. Clasificar si una lesión es benigna o maligna (clasificación binaria).  
2. Aplicar Grad-CAM para interpretar visualmente las decisiones del modelo binario.  
3. Clasificar el tipo específico de lesión maligna mediante aprendizaje contrastivo supervisado.  
4. Evaluar si Grad-CAM puede aplicarse al backbone del modelo contrastivo.  
5. Probar el sistema con una clase maligna no vista durante el entrenamiento (la más pequeña).  
6. Explorar ampliaciones como few-shot learning, clustering y búsqueda por similitud.  

## Flujo del proyecto

### 1. Clasificación binaria (benigna vs maligna)
- Entrenamiento desde cero (modelo CNN básico).  
- Transferencia de aprendizaje con VGG16, ResNet50 e InceptionV3.  
- Comparación de métricas: Accuracy, F1-score, AUC.  
- Distillation del mejor modelo (ResNet50) para obtener una versión ligera.  

### 2. Interpretabilidad con Grad-CAM
- Aplicación de Grad-CAM al modelo binario entrenado.  
- Visualización de regiones relevantes para la clasificación.  
- Preparación de imágenes interpretativas para análisis clínico.  

### 3. Clasificación multiclase entre lesiones malignas
- Entrenamiento de modelo contrastivo (SupConLoss).  
- Generación de embeddings para cada tipo de lesión maligna.  
- Clasificación con k-NN o clasificador lineal sobre embeddings.  

### 4. Ampliaciones
- Visualización de embeddings con t-SNE / UMAP.  
- Búsqueda interactiva por similitud.  
- Embeddings específicos de regiones relevantes (Grad-CAM + contrastivo).  

## Clases del dataset HAM10000

| Clase | Descripción                                        | Tipo     |
|-------|----------------------------------------------------|----------|
| akiec | Queratosis actínicas / carcinoma intraepitelial    | Maligna  |
| bcc   | Carcinoma basocelular                              | Maligna  |
| mel   | Melanoma                                           | Maligna  |
| bkl   | Lesiones benignas tipo queratosis                  | Benigna  |
| df    | Dermatofibroma                                     | Benigna  |
| nv    | Nevos melanocíticos                                | Benigna  |
| vasc  | Lesiones vasculares                                | Benigna  |

## Conclusión

Este proyecto combina clasificación profunda, interpretabilidad visual y análisis de similitud para abordar el diagnóstico automatizado de lesiones cutáneas. La arquitectura jerárquica permite una clasificación binaria inicial seguida de una clasificación multiclase explicable entre lesiones malignas. El uso de Grad-CAM aporta transparencia clínica, mientras que el aprendizaje contrastivo ofrece escalabilidad y adaptabilidad para futuras extensiones. Esta solución tiene potencial para integrarse en entornos médicos reales, facilitando el diagnóstico asistido y la investigación dermatológica.

---

# Project: Classification and Interpretability of Skin Lesions with HAM10000

## Description

This project uses the dataset [**HAM10000**](https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000), which contains dermatoscopic images of seven types of skin lesions. The goal is to build a hierarchical pipeline that allows:

1. Classifying whether a lesion is benign or malignant (binary classification).  
2. Applying Grad-CAM to visually interpret the decisions of the binary model.  
3. Classifying the specific type of malignant lesion using supervised contrastive learning.  
4. Evaluating whether Grad-CAM can be applied to the backbone of the contrastive model.  
5. Testing the system with a malignant class not seen during training (the smallest one).  
6. Exploring extensions such as few-shot learning, clustering, and similarity search.  

## Project Flow

### 1. Binary classification (benign vs malignant)
- Training from scratch (basic CNN model).  
- Transfer learning with VGG16, ResNet50, and InceptionV3.  
- Comparison of metrics: Accuracy, F1-score, AUC.  
- Distillation of the best model (ResNet50) to obtain a lightweight version.  

### 2. Interpretability with Grad-CAM
- Application of Grad-CAM to the trained binary model.  
- Visualization of relevant regions for classification.  
- Preparation of interpretative images for clinical analysis.  

### 3. Multiclass classification among malignant lesions
- Training of a contrastive model (SupConLoss).  
- Generation of embeddings for each type of malignant lesion.  
- Classification with k-NN or linear classifier on embeddings.  

### 4. Extensions
- Visualization of embeddings with t-SNE / UMAP.  
- Interactive similarity search.  
- Region-specific embeddings (Grad-CAM + contrastive).  

## HAM10000 Dataset Classes

| Class | Description                                        | Type     |
|-------|----------------------------------------------------|----------|
| akiec | Actinic keratoses / intraepithelial carcinoma      | Malignant|
| bcc   | Basal cell carcinoma                               | Malignant|
| mel   | Melanoma                                           | Malignant|
| bkl   | Benign keratosis-like lesions                      | Benign   |
| df    | Dermatofibroma                                     | Benign   |
| nv    | Melanocytic nevi                                   | Benign   |
| vasc  | Vascular lesions                                   | Benign   |

## Conclusion

This project combines deep classification, visual interpretability, and similarity analysis to address the automated diagnosis of skin lesions. The hierarchical architecture enables an initial binary classification followed by an explainable multiclass classification among malignant lesions. The use of Grad-CAM provides clinical transparency, while contrastive learning offers scalability and adaptability for future extensions. This solution has the potential to be integrated into real medical environments, facilitating assisted diagnosis and dermatological research.

