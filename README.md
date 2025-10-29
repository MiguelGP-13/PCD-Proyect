“Dermascope: un pipeline contrastivo para detección explicable de lesiones cutáneas”

“Atlas cutáneo: de embeddings contrastivos a Grad-CAM en clasificación de anomalías dermatológicas”

“Perspectivas semánticas: análisis y visualización de anomalías cutáneas mediante aprendizaje contrastivo”

“Conexiones entre lesiones: detección, interpretación y similitud de anomalías cutáneas”

“Detección explicable de lesiones cutáneas: de Grad-CAM a embeddings contrastivos”


# Project: Detection and Localization of Skin Lesion Anomalies with HAM10000

## Description

This project uses the **HAM10000 dataset**, a collection of dermatoscopic images with seven different types of skin lesions. The main goal is to develop a hierarchical pipeline capable of:

1. Classifying the type of skin lesion using a contrastive learning approach.
2. Visualizing the regions responsible for the model’s prediction through Grad-CAM.
3. Measuring similarity between lesions in an embedding space to analyze patterns and relationships.
4. Extending the system to accommodate new lesion classes without retraining the full model.
5. Optionally, clustering embeddings to explore relationships between lesion types and identify ambiguous or rare cases.

This approach aims not only to classify lesions but also to provide added value in interpretability, robustness, and exploratory analysis.

## Workflow

### 1. Multiclass Classification with Contrastive Learning

* Train a **contrastive model** (e.g., Siamese or Triplet Network with SupConLoss) to generate embeddings for the seven lesion types.
* Optionally, attach a **linear classifier** or k-NN on top of embeddings for direct classification.
* The model learns a **semantically meaningful space** where images of the same lesion type are closer and different types are farther apart.

### 2. Interpretability with Grad-CAM

* Apply **Grad-CAM** on the contrastive model backbone.
* Generate heatmaps highlighting the regions responsible for embedding differences or classification decisions.
* Integrate these visualizations to explain why certain lesions are grouped or classified in a specific way.

### 3. Embedding Visualization and Similarity Analysis

* Project contrastive embeddings into a low-dimensional space using **t-SNE or UMAP**.
* Explore clusters to identify patterns between lesion types and subtypes.
* Optional: calculate nearest neighbors to find visually similar lesions (useful for clinical or research insights).

### 4. Extensibility to New Classes

* New lesion classes can be incorporated without retraining the entire backbone:

  * Compute embeddings of new images using the trained model.
  * Classify or cluster using **k-NN** or a small linear classifier on top of embeddings.
* This demonstrates the **scalability and adaptability** of the contrastive approach.

### 5. Optional Enhancements

* **Supervised contrastive regularization:** combine classification loss with SupConLoss to improve embedding separability.
* **Clustering analysis:** validate how embeddings form natural clusters corresponding to lesion types.
* **Ambiguity detection:** identify lesions with high uncertainty or overlapping embeddings.
* **Region-specific embeddings:** extract embeddings from Grad-CAM highlighted regions to focus similarity analysis on clinically relevant areas.

## Selected Classes

The HAM10000 dataset includes seven lesion types:

| Class | Examples                                      |
| ----- | --------------------------------------------- |
| akiec | Actinic keratoses / intraepithelial carcinoma |
| bcc   | Basal cell carcinoma                          |
| bkl   | Benign keratosis-like lesions                 |
| df    | Dermatofibroma                                |
| mel   | Melanoma                                      |
| nv    | Melanocytic nevi                              |
| vasc  | Vascular lesions                              |

## Potential Extensions

* **Few-shot / zero-shot classification:** test pipeline on rare or unseen lesions.
* **Clustering visualization:** t-SNE / UMAP to highlight similarities or outliers.
* **Interactive search:** query similar lesions based on embeddings (option E).
* **Region-focused analysis:** combine Grad-CAM with embeddings to study features driving similarity.

## Conclusion

The project is structured around contrastive embedding learning, interpretability with Grad-CAM, and embedding-based analysis. This architecture provides a scalable, interpretable, and practical solution for automated skin lesion classification and similarity assessment, with potential extensions to new lesion types or clinical applications.

# Proyecto: Detección y Localización de Anomalías en Lesiones Cutáneas con HAM10000

## Descripción

Este proyecto utiliza el **dataset HAM10000**, un conjunto de imágenes dermatoscópicas con siete tipos diferentes de lesiones cutáneas. El objetivo principal es desarrollar un pipeline jerárquico capaz de:

1. Clasificar el tipo de lesión cutánea mediante aprendizaje contrastivo.
2. Localizar visualmente las regiones responsables de la predicción del modelo mediante Grad-CAM.
3. Medir la similitud entre lesiones en un espacio de embeddings para analizar patrones y relaciones.
4. Ampliar el sistema para incorporar nuevas clases de lesiones sin necesidad de reentrenar todo el modelo.
5. Opcionalmente, agrupar embeddings para explorar relaciones entre tipos de lesiones e identificar casos ambiguos o raros.

Este enfoque busca no solo clasificar lesiones, sino también aportar valor añadido en términos de interpretabilidad, robustez y análisis exploratorio.

## Plan de trabajo

### 1. Clasificación multiclase con aprendizaje contrastivo

* Entrenamiento de un **modelo contrastivo** (por ejemplo, red siamesa o triplet con SupConLoss) para generar embeddings de las siete clases de lesión.
* Opcionalmente, añadir un **clasificador lineal** o k-NN sobre los embeddings para clasificación directa.
* El modelo aprende un **espacio semántico** donde imágenes de la misma clase están próximas y diferentes clases alejadas.

### 2. Interpretabilidad con Grad-CAM

* Aplicación de **Grad-CAM** sobre el backbone del modelo contrastivo.
* Generación de mapas de calor que destacan las regiones responsables de las diferencias en embeddings o decisiones de clasificación.
* Integración de estas visualizaciones para explicar por qué ciertas lesiones se agrupan o clasifican de determinada manera.

### 3. Visualización de embeddings y análisis de similitud

* Proyección de embeddings contrastivos en un espacio reducido con **t-SNE o UMAP**.
* Exploración de clusters para identificar patrones entre tipos y subtipos de lesiones.
* Opcional: cálculo de vecinos más cercanos para encontrar lesiones visualmente similares (útil para investigación clínica).

### 4. Ampliación a nuevas clases

* Las nuevas clases de lesiones pueden incorporarse sin reentrenar todo el backbone:

  * Se calculan embeddings de las nuevas imágenes con el modelo entrenado.
  * Se clasifican o agrupan usando **k-NN** o un clasificador lineal pequeño sobre los embeddings.
* Esto demuestra la **escalabilidad y adaptabilidad** del enfoque contrastivo.

### 5. Mejoras opcionales

* **Regularización contrastiva supervisada:** combinar la pérdida de clasificación con SupConLoss para mejorar la separabilidad de embeddings.
* **Análisis de clustering:** validar cómo los embeddings forman clusters naturales correspondientes a tipos de lesión.
* **Detección de ambigüedad:** identificar lesiones con alta incertidumbre o embeddings superpuestos.
* **Embeddings específicos de regiones:** extraer embeddings de zonas señaladas por Grad-CAM para enfocar el análisis en áreas clínicamente relevantes.

## Clases seleccionadas

El dataset HAM10000 incluye siete tipos de lesiones:

| Clase | Ejemplos                                        |
| ----- | ----------------------------------------------- |
| akiec | Queratosis actínicas / carcinoma intraepitelial |
| bcc   | Carcinoma basocelular                           |
| bkl   | Lesiones benignas tipo queratosis               |
| df    | Dermatofibroma                                  |
| mel   | Melanoma                                        |
| nv    | Nevos melanocíticos                             |
| vasc  | Lesiones vasculares                             |

## Posibles ampliaciones

* **Clasificación few-shot / zero-shot:** probar el pipeline con lesiones raras o no vistas.
* **Visualización de clustering:** t-SNE / UMAP para destacar similitudes o outliers.
* **Búsqueda interactiva:** consulta de lesiones similares según embeddings (opción E).
* **Análisis centrado en regiones:** combinar Grad-CAM con embeddings para estudiar características que impulsan la similitud.

## Conclusión

El proyecto se estructura en torno a aprendizaje de embeddings contrastivos, interpretabilidad con Grad-CAM y análisis basado en embeddings. Esta arquitectura proporciona una solución escalable, interpretable y práctica para la clasificación automática de lesiones cutáneas y la evaluación de similitud entre anomalías, con potencial de extensión a nuevas clases o aplicaciones clínicas.
