#Using linear regression to predict the price

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Charger le dataset
df = pd.read_csv("dataset.csv.csv")

# Définir les variables explicatives (Année, Kilométrage) et la cible (Prix)
X = df[["Année", "Kilométrage"]]
y = df["Prix"]

# Séparer les données en ensemble d'entraînement et de test (80% - 20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Créer et entraîner le modèle
model = LinearRegression()
model.fit(X_train, y_train)

# Afficher les coefficients appris
print(f"Intercept: {model.intercept_}")
print(f"Coef_Année: {model.coef_[0]}, Coef_Kilométrage: {model.coef_[1]}")

import joblib

# Sauvegarder le modèle dans un fichier local
joblib.dump(model, "linear_regression_model.pkl")

print("Modèle sauvegardé avec succès !")

# Charger le modèle entraîné
model = joblib.load("linear_regression_model.pkl")

# Exemple : prédire le prix d'une MT-07 de 2016 avec 20 000 km
annee_test = 2015
kilometrage_test = 44100

prix_prevu = model.predict([[annee_test, kilometrage_test]])[0]
print(f"Prix estimé pour une MT-07 de {annee_test} avec {kilometrage_test} km : {prix_prevu:.2f} €")

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(df["Année"], df["Kilométrage"], df["Prix"], color='blue', label="Données réelles")

ax.set_xlabel("Année")
ax.set_ylabel("Kilométrage")
ax.set_zlabel("Prix")
ax.set_title("Prix en fonction de l'année et du kilométrage")

plt.legend()
plt.show()
