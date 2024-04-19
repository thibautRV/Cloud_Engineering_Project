FROM python:3.11.9-bullseye

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie les fichiers requis pour l'installation des dépendances
COPY . .

# Installe les dépendances
RUN pip install --no-cache-dir -r https://raw.githubusercontent.com/thibautRV/Cloud_Engineering_Project/main/dashboard/requirements.txt

# Copie les fichiers de l'application Streamlit dans le conteneur
COPY . /app

# Expose le port sur lequel Streamlit s'exécute
EXPOSE 8501

# Commande pour exécuter l'application Streamlit
CMD ["streamlit", "run", "dashboard.py", "--server.port=8501", "--server.headless=true", "--server.address=0.0.0.0"]
