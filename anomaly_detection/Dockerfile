FROM python:3.11.9-bullseye

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie les fichiers requis pour l'installation des dépendances
COPY . .

# Installe les dépendances
RUN pip install --no-cache-dir -r https://raw.githubusercontent.com/thibautRV/Cloud_Engineering_Project/main/anomaly_detection/requirements.txt

# Copie les fichiers de l'application Streamlit dans le conteneur
COPY . /app

# Commande pour exécuter l'application Streamlit
CMD ["python", "anomaly_detector.py"]
