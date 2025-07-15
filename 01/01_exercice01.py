# Demande d'information à l'utilisateur


prenom = str(input("Entrez votre prénom svp: "))
age = int(input("Entrez votre âge svp: "))
ville = str(input("Entrez votre ville svp: "))
metier = str(input("Entrez votre métier svp: "))

# Approximation des jours vécus

jours_vecu = age * 365

# Affichage formaté

print(f'\n==== PROFIL UTILISATEUR ====')
print(f'Prénom: {prenom}')
print(f'Âge: {age} ans {jours_vecu} jours vécus environ')
print(f'Ville: {ville}')
print(f'Métier: {metier}')


