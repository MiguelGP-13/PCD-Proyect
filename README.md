# PCD-Proyect
## Options contemplated
### Option 1: Urban segmentation + scene reasoning
Use a segmentation model (U-Net, DeepLab, Mask R-CNN) on urban images and apply rules to interpret the scene. Examples: count pedestrians at crosswalks, detect cars in bike lanes, or measure traffic density.  
Dataset: [Cityscapes](https://www.cityscapes-dataset.com/)

### Option 2: Autoencoders for industrial anomaly detection
Train a convolutional autoencoder to reconstruct images of defect-free industrial parts and use reconstruction error to detect anomalies (cracks, scratches, deformations).  
Dataset: [MVTec AD](https://www.mvtec.com/company/research/datasets/mvtec-ad)

### Option 3: CLIP for video in the movie domain
Apply a VideoCLIP-style model on movie clips with subtitles and descriptions to align video and text. Enables semantic search such as “night car chase” and retrieves the corresponding clips.  
Dataset: [Condensed Movies](https://www.robots.ox.ac.uk/~vgg/data/condensed-movies/)

## Proyecto: Style Transfer Multiclase con Segmentación Semántica y Style Blending

### Descripción
Este proyecto combina **segmentación semántica** y **neural style transfer** para aplicar **diferentes estilos artísticos a distintas regiones de una misma imagen urbana**.  
El objetivo es generar resultados **vistosos, coherentes y explicables**, donde cada clase semántica (por ejemplo, edificios, cielo, coches, vegetación) pueda recibir un estilo distinto (cubismo, impresionismo, puntillismo, etc.).

El componente clave es el **style blending**:
- Permite transiciones suaves entre regiones estilizadas.  
- Evita bordes duros y artefactos visuales.  
- Da flexibilidad para expandir o suavizar las máscaras segmentadas, logrando que los objetos (por ejemplo, coches en cubismo) tengan más presencia visual sin romper la coherencia de la escena.

### Pipeline
1. **Segmentación semántica** de la imagen de contenido (ejemplo: foto urbana de Madrid).  
2. **Selección de estilos**: para cada clase segmentada se asigna un estilo artístico.  
   - Se eligen varias imágenes de un mismo estilo y se calcula una **media de features** para mayor consistencia.  
3. **Aplicación de style transfer por clase** con blending en los bordes.  
4. **Composición final** de la imagen estilizada multiclase.  

### Datasets
- **Cityscapes** (entrenamiento/validación de segmentación urbana):  
  [Cityscapes Dataset](https://www.cityscapes-dataset.com/)  

- **Imágenes urbanas de Madrid** (para test):  
  - **Mapillary Vistas Dataset** (contiene escenas urbanas de todo el mundo, incluidas de España):  
    [Mapillary Vistas](https://www.mapillary.com/dataset/vistas)  
  - También se pueden usar imágenes propias o de dominio público.  

- **WikiArt** (estilos artísticos, más de 80.000 obras en 27 estilos):  
  [WikiArt en Kaggle](https://www.kaggle.com/datasets/steubk/wikiart)  

## Posibles extensiones
- Interfaz interactiva para reasignar estilos a clases.  
- Interpolación de estilos (por ejemplo, edificios mitad cubistas y mitad futuristas).  
- Aplicación a secuencias de vídeo con coherencia temporal.  
