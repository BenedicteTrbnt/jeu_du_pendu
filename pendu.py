#déclaration des variables globales et importations
import os
import random
global lettres_donnees
global lettres_a_deviner
global rejouer
rejouer='oui'
global nombre_chances
global mot
import string

# chaines de caracteres contenant l'alphabet en minuscule et majuscule
alphabet_min=string.ascii_lowercase
alphabet_maj=string.ascii_uppercase


# choix du fichier de mots pour le jeu, avec le fichier par défaut
choix=str(input('Vous voulez vous utiliser votre propre fichier de mots sinon une liste de mots sera utilisée par défaut par ce script ? Répondre par oui ou non'))

if choix=='non':
    chemin=('/Users/beneturbant/Documents/ETS/SE24/MGA802/mots.txt')
elif choix=='oui':
    nom_fichier=str(input('Quel est le nom du fichier ?'))
    dossier_fichier=str(input('Quel est le chemin du fichier ?'))
    chemin= os.path.join(dossier_fichier, nom_fichier)
else:
    print('Vous n\'avez pas répondu à la question par oui ou non, veuillez rélancer le jeu')
    exit()

# lecture du fichier et création de la liste de mots
with open(chemin,'r',encoding='utf8') as fio:
    words=fio.read().splitlines()


# fonction qui permet de choisir aléatoirement un mot dans le fichier de la liste de mots
def choisir_mot(a):
    return random.choice(a)

# fonction pour unifier le mot si il contient des caractères spéciaux comme des accents
def unifier(b):
    from unicodedata import normalize
    return(normalize('NFD',b).encode('ASCII', 'ignore').decode('utf8'))

#fonction du jeu du pendu, la fonction retourne la variable rejouer
def pendu():
    mot_aleatoire = choisir_mot(words)
    mot=unifier(mot_aleatoire)
    mot_longueur = len(mot)
    mot_a_deviner = '_' * mot_longueur
    nombre_chances = 6
    lettres_donnees = ''
    lettres_a_deviner=''
    # boucle tant que le nombre de chances restant est supérieur à 0
    while nombre_chances>0:
        # cas si le mot n'a pas encore été trouvé
        if mot_a_deviner!=mot:
            print('devinez le mot suivant: ',mot_a_deviner)
            # cas si il reste 1 seule chance avec affichage d'un indice
            if nombre_chances==1:
                for j in range(mot_longueur):
                    place=alphabet_min.find(mot[j])
                    lettres_a_deviner=alphabet_min[:place]+alphabet_min[place+1:len(alphabet_min)]
                indice=random.choice(lettres_a_deviner)
                print('Un indice, la lettre ',indice, ' n\'est pas dans le mot')
            # demande d'un lettre à l'utilisateur
            lettre=str(input('Entrez une lettre !'))
            # vérification que la variable entrée par l'utilisateur est bien une lettre (minuscule ou majusucle)
            if lettre in alphabet_min or lettre in alphabet_maj:
                # cas si la lettre a déjà été donnée par l'utilisateur
                if lettre in lettres_donnees:
                    print('Cette lettre à déjà été donnée, il te reste toujours ', nombre_chances, ' chance(s) pour deviner le mot')
                else:
                    lettres_donnees +=lettre
                    # cas si la lettre est dans le mot
                    if lettre in mot:
                        for i in range(mot_longueur):
                            if mot[i]==lettre:
                                mot_a_deviner=mot_a_deviner[:i]+lettre+mot_a_deviner[i+1:mot_longueur]
                        print('Bravo cette lettre est dans le mot')
                        print('Il te reste ', nombre_chances, ' chance(s) pour deviner le mot')
                    # cas si la lettre donnée n'est pas dans le mot avec le nombre de chances qui
                    # diminue
                    else:
                        nombre_chances -= 1
                        print('Dommage cette lettre n\'est pas dans le mot')
                        print('Il te reste ', nombre_chances, ' chance(s) pour deviner le mot')
            else:
                print('Veuillez saisir une lettre de l\'alphabet')
        # cas si le mot est trouvé et demande à l'utilisateur si il veut rejouer ou non
        else :
            print('Bravo vous avez deviné le mot ', mot_a_deviner,' !')
            rejouer=str(input('Voulez vous rejouer ? Répondre par oui ou non'))
            if rejouer != 'oui':
                exit()
            else:
                return(rejouer)

    # cas si l'utilisateur a perdu, et demande si il veut rejouer ou non
    if nombre_chances==0:
        print('Dommage vous avez perdu, le mot à deviner était ',mot)
        rejouer = str(input('Voulez vous rejouer ? Répondre par oui ou non'))
        if rejouer!='oui':
            exit()
        else:
            return(rejouer)

# boucle tant que rejouer=='oui' alors le jeu du pendu est relancé.
while rejouer=='oui':
    pendu()
    if not rejouer=='oui':
        exit()

