import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os

CSV_FILE = "dataset.csv"

if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(columns=[ "Prix","Année", "Kilométrage", "Modèle"])
    df.to_csv(CSV_FILE, index=False)

def save_entry():
    annee = entry_annee.get()
    kilometrage = entry_km.get()
    prix = entry_prix.get()
    modele = entry_modele.get()
    
    if not (annee and kilometrage and prix and modele):
        messagebox.showwarning("Erreur", "Veuillez remplir tous les champs.")
        return
    
    try:
        annee = int(annee)
        kilometrage = int(kilometrage)
        prix = int(prix)
    except ValueError:
        messagebox.showwarning("Erreur", "Année, Kilométrage et Prix doivent être numériques.")
        return
    
    new_data = pd.DataFrame([[prix, annee, kilometrage, modele]], columns=["Prix", "Année", "Kilométrage", "Modèle"])
    new_data.to_csv(CSV_FILE, mode='a', header=False, index=False)
    
    messagebox.showinfo("Succès", "Donnée ajoutée avec succès !")
    entry_prix.delete(0, tk.END)
    entry_annee.delete(0, tk.END)
    entry_km.delete(0, tk.END)
    entry_modele.delete(0, tk.END)
    
root = tk.Tk()
root.title("Ajout de données moto")

tk.Label(root, text="Prix").grid(row=0, column=0)
entry_prix = tk.Entry(root)
entry_prix.grid(row=0, column=1)


tk.Label(root, text="Année").grid(row=1, column=0)
entry_annee = tk.Entry(root)
entry_annee.grid(row=1, column=1)

tk.Label(root, text="Kilométrage").grid(row=2, column=0)
entry_km = tk.Entry(root)
entry_km.grid(row=2, column=1)

tk.Label(root, text="Modèle").grid(row=3, column=0)
entry_modele = tk.Entry(root)
entry_modele.grid(row=3, column=1)
entry_modele.insert(0, "MT 07")

tk.Button(root, text="Enregistrer", command=save_entry).grid(row=4, columnspan=2)

root.mainloop()
