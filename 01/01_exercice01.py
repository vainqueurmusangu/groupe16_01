# Demande d'information à l'utilisateur

try:
    prenom = str(input("Entrer votre prénom svp: "))
    age = int(input("Entrer votre âge svp: "))
    ville = str(input("Entrer votre ville svp: "))
    metier = str(input("Entrez votre métier svp: "))

    # Approximation des jours vécus

    jours_vecu = age * 365

    # Affichage formaté

    print(f'\n==== PROFIL UTILISATEUR ====')
    print(f'Prénom: {prenom}')
    print(f'Âge: {age} ans {jours_vecu} jours vécus environ')
    print(f'Ville: {ville}')
    print(f'Métier: {metier}')
except ValueError:
    print("bonjour")
    print(f'Veillez saisir les données valides svp!')

