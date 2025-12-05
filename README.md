# TODO - Proyecto HAM10000

## Clasificación full
- [x] Probar desde cero
- [x] Probar fine tuning con VGG19
- [x] Comparar con pipeline

## Clasificación binaria
- [x] Entrenar modelo desde cero
- [x] Transfer learning con VGG16
- [x] Transfer learning con ResNet50
- [x] Transfer learning con InceptionV3
- [x] Tener todos entrenados y guardados
  

- [x] Comparar métricas

## Grad-CAM
- [x] Aplicar Grad-CAM al mejor modelo binario
- [x] Generar imágenes interpretativas
- [x] Documentar visualizaciones

## Clasificación contrastiva
- [x] Entrenar modelo contrastivo (SupConLoss)
- [x] Generar embeddings
- [x] Clasificar con k-NN o lineal (?) Da 60%, explicar comparacion entre supConloss y por pares
- [x] Probar ml normal en malignas
- [x] Visualizar con t-SNE / UMAP

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
| mel   | Melanoma                                            | Maligna  |
| bkl   | Lesiones benignas tipo queratosis                  | Benigna  |
| df    | Dermatofibroma                                      | Benigna  |
| nv    | Nevos melanocíticos                                 | Benigna  |
| vasc  | Lesiones vasculares                                 | Benigna  |

## Conclusión

Este proyecto combina clasificación profunda, interpretabilidad visual y análisis de similitud para abordar el diagnóstico automatizado de lesiones cutáneas. La arquitectura jerárquica permite una clasificación binaria inicial seguida de una clasificación multiclase explicable entre lesiones malignas. El uso de Grad-CAM aporta transparencia clínica, mientras que el aprendizaje contrastivo ofrece escalabilidad y adaptabilidad para futuras extensiones. Esta solución tiene potencial para integrarse en entornos médicos reales, facilitando el diagnóstico asistido y la investigación dermatológica.
