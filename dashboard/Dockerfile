FROM python:3.8

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie les fichiers requis pour l'installation des dépendances
COPY . .

# Installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copie les fichiers de l'application Streamlit dans le conteneur
COPY . /app

# Expose le port sur lequel Streamlit s'exécute
EXPOSE 8501

# Commande pour exécuter l'application Streamlit
CMD ["streamlit", "run", "dashboard.py"]
