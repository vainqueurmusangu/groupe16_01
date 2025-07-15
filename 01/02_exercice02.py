# Définition des variables

nom_produit = "Casque Bluetooth"
prix = 150.0
stock = 35
remise = 0.15   # 15%

# calcul du prix final
prix_final = prix * (1 - remise)

# Affichage

print(f'Poduit: {nom_produit}')
print(f'Prix initial: {prix} $')
print(f'Remise: {remise * 100}%')
print(f'Prix final: {prix_final:.2f}$')
print(f'Stock disponible: {stock}')