# Importer les bibliothèques nécessaires
import datetime

# Créer une liste vide pour stocker les activités
activites = []

# Définir une fonction pour ajouter une nouvelle activité
def ajouter_activite():
    # Demander à l'utilisateur de saisir les détails de l'activité
    nom = input("Nom de l'activité : ")
    date_str = input("Date de l'activité (JJ-MM-AAAA) : ")
    heure_str = input("Heure de l'activité (HH:MM) : ")
    lieu = input("Lieu de l'activité : ")
    
    # Convertir la date et l'heure en format datetime
    date = datetime.datetime.strptime(date_str, '%d-%m-%Y')
    heure = datetime.datetime.strptime(heure_str, '%H:%M')
    date_et_heure = datetime.datetime.combine(date, heure.time())
    
    # Ajouter l'activité à la liste des activités
    activites.append({
        'nom': nom,
        'date_et_heure': date_et_heure,
        'lieu': lieu
    })
    
    print("Activité ajoutée avec succès.")

# Définir une fonction pour afficher les activités planifiées
def afficher_activites():
    print("Voici les activités planifiées :")
    
    for activite in activites:
        print("- {} le {} à {} à {}.".format(
            activite['nom'],
            activite['date_et_heure'].strftime('%d-%m-%Y'),
            activite['date_et_heure'].strftime('%H:%M'),
            activite['lieu']
        ))

# Boucle principale du programme
while True:
    # Afficher le menu principal
    print("\nQue souhaitez-vous faire ?")
    print("1. Ajouter une activité")
    print("2. Afficher les activités planifiées")
    print("3. Quitter")
    
    choix = input("Votre choix : ")
    
    # Traiter le choix de l'utilisateur
    if choix == "1":
        ajouter_activite()
    elif choix == "2":
        afficher_activites()
    elif choix == "3":
        print("Au revoir !")
        break
    else:
        print("Choix invalide. Veuillez choisir une option valide.")

