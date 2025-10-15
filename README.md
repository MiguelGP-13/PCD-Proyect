# PCD-Proyect
## Optiosn contemplated
### Option 1: Urban segmentation + scene reasoning
Use a segmentation model (U-Net, DeepLab, Mask R-CNN) on urban images and apply rules to interpret the scene. Examples: count pedestrians at crosswalks, detect cars in bike lanes, or measure traffic density.  
Dataset: [Cityscapes](https://www.cityscapes-dataset.com/)

### Option 2: Autoencoders for industrial anomaly detection
Train a convolutional autoencoder to reconstruct images of defect-free industrial parts and use reconstruction error to detect anomalies (cracks, scratches, deformations).  
Dataset: [MVTec AD](https://www.mvtec.com/company/research/datasets/mvtec-ad)

### Option 3: CLIP for video in the movie domain
Apply a VideoCLIP-style model on movie clips with subtitles and descriptions to align video and text. Enables semantic search such as “night car chase” and retrieves the corresponding clips.  
Dataset: [Condensed Movies](https://www.robots.ox.ac.uk/~vgg/data/condensed-movies/)

