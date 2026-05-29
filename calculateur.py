def calculer_tva(prix_ht: float) -> float:
    return prix_ht * 1.20


prix_ttc = calculer_tva(100)
print(f"Total TTC: {prix_ttc}")

def calculer_pourboire(montant, taux_pourboire):
    return montant * taux_pourboire / 100

pourboire = calculer_pourboire(100, 15)
print(f"Pourboire : {pourboire} €")