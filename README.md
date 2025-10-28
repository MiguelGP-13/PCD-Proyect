Nombres:
"Ojos industriales: un pipeline modular para detectar, explicar y clasificar anomalías"

"Perspectivas contrastivas: detección explicable de anomalías en inspección visual industrial"

"Tendiendo puentes entre detección y explicación: un pipeline multi-etapa para anomalías industriales"

"Atlas de anomalías: detección, localización y clasificación contrastiva en imágenes industriales"

"Detección explicable de anomalías industriales: de Grad-CAM a embeddings contrastivos"

# Proyecto: Detección y Localización de Anomalías en Procesos Industriales con MVTec AD

## Descripción
Este proyecto utiliza el dataset **MVTec AD**, un conjunto de imágenes industriales diseñado específicamente para la detección de anomalías. El objetivo principal es desarrollar un pipeline jerárquico capaz de:

1. Detectar si una imagen es anómala o no.
2. Localizar visualmente las regiones responsables de la predicción mediante Grad-CAM.
3. Verificar casos ambiguos con un autoencoder entrenado únicamente con imágenes normales.
4. Clasificar el tipo de anomalía utilizando modelos contrastivos especializados por clase de objeto.
5. Visualizar en un espacio reducido las distancias entre anomalías para analizar similitudes y patrones.

Este enfoque busca no solo resolver la tarea de detección, sino también aportar valor añadido en términos de explicabilidad, robustez y análisis exploratorio.

## Plan de trabajo

### 1. Clasificación binaria (normal vs anómala)
- Entrenamiento de un modelo supervisado (ResNet, EfficientNet) para distinguir entre imágenes normales y defectuosas.
- Evaluación mediante métricas de clasificación (AUC, F1-score, precisión, recall).
- Este modelo constituye la primera capa de decisión del pipeline.

### 2. Interpretabilidad con Grad-CAM
- Aplicación de Grad-CAM sobre el clasificador binario.
- Generación de mapas de calor que señalen las regiones responsables de la predicción de anomalía.
- Integración de estas visualizaciones en el pipeline para facilitar la explicación de resultados.

### 3. Verificación con autoencoder en casos ambiguos
- Entrenamiento de un autoencoder únicamente con imágenes normales.
- Uso del error de reconstrucción como métrica de anomalía.
- Aplicación en casos de baja confianza del clasificador binario (probabilidades cercanas al umbral).
- Valor añadido: robustez y reducción de falsos positivos/negativos.

### 4. Clasificación del tipo de anomalía con modelos contrastivos
- Entrenamiento de un modelo contrastivo (SimCLR, SupCon) **por clase de objeto**.
- Dentro de cada categoría, el modelo aprende a separar los distintos tipos de defectos (ej. en *capsule*: crack, faulty imprint, scratch).
- Clasificación de anomalías mediante comparación de embeddings con prototipos de cada tipo.
- Valor añadido: organización y priorización de defectos según su naturaleza.

### 5. Visualización de distancias entre anomalías
- Proyección de los embeddings contrastivos en un espacio reducido (t-SNE, UMAP).
- Representación gráfica de las distancias entre anomalías para identificar similitudes y agrupaciones.
- Valor añadido: análisis exploratorio y explicación visual de cómo se relacionan los defectos entre sí.

## Categorías seleccionadas
Se han seleccionado 7 categorías de objetos del dataset MVTec AD, priorizando aquellas con mayor número de imágenes defectuosas para garantizar un entrenamiento robusto:

| Categoría   | Ejemplos de defectos |
|-------------|----------------------|
| bottle      | contamination, defectos en el cuello |
| cable       | roturas, hilos sueltos |
| capsule     | crack, faulty imprint, scratch |
| metal nut   | defectos de forma, contaminación |
| pill        | grietas, impresión defectuosa |
| screw       | cabezas deformadas, defectos pequeños |
| zipper      | dientes defectuosos, deformaciones |

## Opciones de ampliación
- **Clasificación de categoría**: Clasificar la categoría al inicio
- **Segmentación semántica:** entrenar un modelo de segmentación (U-Net, DeepLabV3+) con las máscaras de anomalía del dataset para obtener localización a nivel de píxel.  
- **Reconstrucción generativa:** entrenar un modelo generativo (VAE, GAN) para reconstruir imágenes normales y resaltar anomalías mediante mapas de diferencia.  
- **Fusión multimodal:** integrar descripciones textuales de defectos y entrenar un modelo tipo CLIP para búsqueda semántica.  
- **Evaluación few-shot/zero-shot:** probar la capacidad del pipeline para generalizar a defectos no vistos durante el entrenamiento.

## Conclusión
El proyecto se estructura en cinco fases: detección inicial, interpretabilidad, verificación con autoencoder, clasificación contrastiva por objeto y visualización de similitudes. Esta arquitectura permite evolucionar de un sistema básico de detección a una solución integral de inspección industrial automatizada, con un alto grado de explicabilidad y aplicabilidad práctica.
