FROM python:3.9

WORKDIR /app

# Copier le code de l'API dans le répertoire de travail
COPY mlops/api/ /app/

# Copier le modèle entraîné
COPY mlops/model/model.pkl /app/

# Installer les dépendances nécessaires
RUN pip install Flask joblib scikit-learn

# Exposer le port 5000 pour l'API Flask
EXPOSE 5003

# Commande pour lancer l'API
CMD ["python", "main.py"]
