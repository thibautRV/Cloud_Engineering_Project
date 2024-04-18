# Utiliser l'image officielle de PostgreSQL
FROM postgres:latest

# Définir les variables d'environnement pour le mot de passe de l'administrateur
# et le nom de la base de données (à personnaliser selon vos besoins)
ENV POSTGRES_PASSWORD=datasql78$
ENV POSTGRES_DB=NumericFarm

# Exposer le port (5432 est le port par défaut de PostgreSQL)
EXPOSE 5432

# Install curl if it's not already in the image
RUN apt-get update && apt-get install -y curl

# Download the schema.sql file into the docker-entrypoint-initdb.d directory
RUN curl -o /docker-entrypoint-initdb.d/schema.sql https://raw.githubusercontent.com/thibautRV/Cloud_Engineering_Project/main/database/schema.sql

# Aucune commande CMD n'est nécessaire ici, car nous utilisons les comportements par défaut de l'image postgres
