import os

# Definición de la estructura
structure = {
    "data": ["raw", "processed"],
    "train": [
        "1_classifier_gradcam.ipynb",
        "2_autoencoder.ipynb",
        "3_contrastive_visualization.ipynb",
    ],
    "models": ["classifier", "autoencoder", "contrastive"],
    "docs": [],
}

# Crear carpetas y archivos
for folder, contents in structure.items():
    os.makedirs(folder, exist_ok=True)
    for item in contents:
        path = os.path.join(folder, item)
        if "." in item:  # es archivo
            if not os.path.exists(path):
                open(path, "w").close()
        else:  # es subcarpeta
            os.makedirs(path, exist_ok=True)

# Archivos raíz
root_files = ["result.ipynb", "requirements.txt"]
for f in root_files:
    if not os.path.exists(f):
        open(f, "w").close()

# README en subcarpetas clave
with open("data/README.md", "w") as f:
    f.write("# Data\n\nColoca aquí los datos crudos en `raw/` y los preprocesados en `processed/`.\n")

with open("models/README.md", "w") as f:
    f.write("# Models\n\nAquí se guardarán los pesos entrenados de cada modelo.\n")

print("Estructura del proyecto creada con éxito.")
