    return prix_ht * 1.20
def calculer_tva(prix_ht: float) -> float:


prix_ttc = calculer_tva(100)
print(f"Total TTC: {prix_ttc}") 


def calculer_tva(prix_ht, taux_tva):
    return prix_ht * 120

prix_ttc = calculer_tva(100)
print(f"total TTC: {prix_ttc}")
