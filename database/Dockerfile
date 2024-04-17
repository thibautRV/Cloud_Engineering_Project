# Utiliser l'image officielle de PostgreSQL
FROM postgres:latest

# Définir les variables d'environnement pour le mot de passe de l'administrateur
# et le nom de la base de données (à personnaliser selon vos besoins)
ENV POSTGRES_PASSWORD=datasql78$
ENV POSTGRES_DB=urban_farm

# Exposer le port (5432 est le port par défaut de PostgreSQL)
EXPOSE 5432

# Copier le fichier schema.sql dans le dossier /docker-entrypoint-initdb.d
# pour qu'il soit exécuté lors de l'initialisation de la base de données
COPY schema.sql /docker-entrypoint-initdb.d/

# Aucune commande CMD n'est nécessaire ici, car nous utilisons les comportements par défaut de l'image postgres
