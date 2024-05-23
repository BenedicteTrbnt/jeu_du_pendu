Pseudocode

Premièrement demander à lutilisateur si il veut utiliser son propre fichier ou le fichier par défaut à l'aide d'un input
if oui 
  demander le nom du fichier et le chemin

Lire le fichier et créer la liste de mots à l'aide de
with open(chemin,'r',encoding='utf8') as fio:
    words=fio.read().splitlines()

Créer une fonction choisr_mot qui permet de choisir un mot aléatoirement dans la liste de mots à l'aide de random

Créer une fonction unifier pour unifier le mot si il contient des caractères spéciaux comme des accents
  utiliser normalize de unicodedata

initialiser rejouer=='oui'

Créer une fonction pendu
  utiliser la fonction choisir_mot pour choisir un mot aléatoire
  utiliser la fonction unifier pour unifier le mot
  initialisation des variables : 
  mot_longueur
  nombre_de_chances=6
  lettres_données
  lettres_a_deviner
  boucle while tant que le nombre de chance est supérieur à 0
    if le mot n'a pas encore été trouvé
      if il reste un chance donner un indice
        utiliser la fonction random pour afficher aléatoirement une lettre qui n'est pas dans le mot
      demander une à l'utilisateur de donner une lettre (input)
      vérifier que la variable entrée est bien une lettre et qu'elle n'a pas déja été donnée
      ajouter la lettre a lettre_donnees
      if la lettre est dans le mot
        afficher la lettre à la place du _ dans le mot
        indiquer à l'utilisateur que la lettre est dans le mot, et le nombre de chance(s) restante(s) avec un print
      else (la lettre n'est pas dans le mot)
        nombre_chances-=1
        indiquer à l'utilisateur que la lettre n'est pas dans le mot, et le nouveau nombre de chance(s) restante(s) avec un print
    else le mot a été trouvé
      indiquer à l'utilisateur qu'il a trouvé le mot avec un print  
      avec un input il demander si il veut rejouer (oui ou non)
        if rejouer=='oui':
          return(rejouer)
        else:
          exit()
  fin de la boucle while

  if nombre_chances==0
    indiquer à l'utilisateur qu'il a perdu et lui donner le mot qu'il devait trouver avec un print
    avec un input il demander si il veut rejouer (oui ou non)
      if rejouer=='oui':
        return(rejouer)
      else:
        exit()

fin de la fonction pendu

création du boucle pour (re)lancer tant que le joueur veut rejouer
boucle while tant que rejouer=='oui'
  pendu()
  if not rejouer=='oui'
    exit()






        
  
