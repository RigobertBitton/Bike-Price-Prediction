from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Configuration de Selenium
options = Options()
options.add_argument("--headless")  # Mode sans interface graphique
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

# Lancer le navigateur
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# URL cible
url = "https://www.leboncoin.fr/recherche?category=3&locations=r_12&cubic_capacity=600-700&u_moto_brand=YAMAHA&moto_type=moto&u_moto_model=YAMAHA_MT"
driver.get(url)

# Attendre le chargement
time.sleep(5)

# Récupération des annonces
annonces = driver.find_elements(By.CLASS_NAME, "_34f6D")  # Classe CSS des annonces

data = []
for annonce in annonces:
    try:
        titre = annonce.find_element(By.CLASS_NAME, "_2tubl").text  # Nom de la moto
        prix = annonce.find_element(By.CLASS_NAME, "_2xIl6").text   # Prix
        details = annonce.find_elements(By.CLASS_NAME, "_1G5Hc")  # Détails (année, km)
        
        # Extraire année et km si dispo
        annee, km = "N/A", "N/A"
        if len(details) >= 2:
            annee, km = details[0].text, details[1].text
        
        data.append([titre, prix, annee, km])
    except Exception as e:
        print(f"Erreur : {e}")

# Fermer le navigateur
driver.quit()

# Sauvegarde des données
df = pd.DataFrame(data, columns=["Titre", "Prix", "Année", "Kilométrage"])
df.to_csv("motos_leboncoin.csv", index=False)
print("Scraping terminé, fichier CSV enregistré.")
