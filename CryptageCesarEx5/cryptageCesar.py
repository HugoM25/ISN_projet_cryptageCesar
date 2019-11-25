
#les fonctions de cryptage ci dessous ont été prevues pour suivre un decalage cohérent avec celui de la question 4 :
#Le message sera en minuscule et les apostrophes, les ponctuations ainsi que les espaces ne changeront pas.
#Le message ne comprendra aussi aucun accent ni chiffre

# la fonction de cryptage :

def Cryptage(mot, key):
    #On lower chaque lettre pour éviter que leur code ascii soit différent de celui attendu
    mot = mot.lower()
    #On crée une chaîne de caractères vide dans laquelle on écrira le message codé
    motcache = ""
    #Si la clé dépasse le nombre de décalage possible on va la réduire ou l'augmenter si elle est en dessous de -26
    if key >0 :
        while key > 26 :
            key -=26
    if key < 0 :
        while key < -26 :
            key +=26
    #On code chaque lettre
    for lettre in mot :
        # On prend le code ascii de la lettre
        crl = ord(lettre)
        # Si le code est différent d'un signe de ponctuation ou d'un apostrophe on code la lettre
        if (crl != 32 and crl != 39 and crl != 46 and crl != 63 and crl != 33 and crl != 44 ) :
            # On ajoute le décalage (si la clé est négative c'est comme si on reculait de n lettres)
            crl += key
            # Si le code dépasse les caractères minuscules (donc le z) on boucle en enlevant 26
            if (crl> 122):
                crl -= 26
            # Si le code descend en dessous de a on boucle aussi en ajoutant 26
            elif (crl < 97):
                crl += 26
            #On ajoute le charactère associé à la lettre au mot final
            motcache += chr(crl)
        else :
            # Si la lettre est un symbole on ne la change pas, on l'ajoute juste
            motcache += lettre
    #On retourne le mot codé à la fin
    return( motcache)

#la fonction de decryptage quand la clé est connue

def Decryptage(mot, key) :
    #On lower chaque lettre pour éviter que leur code ascii soit différent de celui attendu
    mot = mot.lower()
    #On crée une chaîne de caractères vide dans laquelle on écrira le message décodé
    motdecode = ""
    #Si la clé dépasse le nombre de décalage possible on va la réduire ou l'augmenter si elle est en dessous de -26
    if key >0 :
        while key > 26 :
            key -=26
    if key < 0 :
        while key < -26 :
            key +=26
     #On code chaque lettre
    for lettre in mot :
        # On prend le code ascii de la lettre
        crl = ord(lettre)
        # Si le code est différent d'un signe de ponctuation ou d'un apostrophe on décode la lettre
        if (crl != 32 and crl != 39 and crl != 46 and crl != 63 and crl != 33 and crl != 44 ) :
            # On ajoute le décalage inverse pour faire retrouver la lettre avant le codage
            crl += -key
            # Si le code dépasse les caractères minuscules (donc le z) on boucle en enlevant 26
            if (crl> 122):
                crl -= 26
            # Si le code descend en dessous de a on boucle aussi en ajoutant 26
            elif (crl < 97):
                crl += 26
            #On ajoute le charactère associé à la lettre au mot final
            motdecode += chr(crl)
        else :
            # Si la lettre est un symbole on ne la change pas, on l'ajoute juste
            motdecode += lettre
    #On retourne le mot décodé à la fin
    return( motdecode)

#Un programme pour brute-forcer la clé en parcourant toutes les possibilités
#Permettant par exemple de trouver : les profs d'isn sont les meilleurs!. :
#BruteForce("wpd aczqd o'tdy dzye wpd xptwwpfcd!.")


def BruteForce(mot) :
    mot = mot.lower()
    motdecode = ""
    '''Petite liste de mots assez fréquents dans les phrases francaises qui va nous permettre plus tard de
    déterminer les potentielles phrases après décodage.'''
    listmotsfrequents = ["je", "tu", "il", "elle","on" ,"nous" ,"vous", "ils", "elles" ,"suis" , "est", "sommes", "etes", "sont", "ont", "etre" ,"avoir" ,"a", "le", "la", "les", "ce" ,"se"]
    phrasesprobables = []
    #On va effectuer le même système de décodage que dans la fonction d'avant mais en le faisant avec chaque clé possible (de 0 à 26 non compris car ceci reviendrais, comme avec 0, à ne rien bouger).

    for i in range(0,26):
        motdecode = ""
        for lettre in mot :
            crl = ord(lettre)
            if (crl != 32 and crl != 39 and crl != 46 and crl != 63 and crl != 33 and crl != 44 ) :
                crl += i
                if (crl> 122):
                    crl -= 26
                elif (crl < 97):
                    crl += 26
                motdecode += chr(crl)
            else :
                motdecode+= lettre

        # cette partie permet de chercher si le mot trouvé peut correspondre à une phrase francaise en se fiant au dictionnaire (un peu petit) défini dans la liste nommée listmotsfrequents
        phrsplit = []
        #Divise le message en plusieurs mots distincts en coupant à chaque espace
        phrsplit = motdecode.split()
        proba = 0
        #Cette boucle vérifie si un mot dans le message décodé avec une des clé est contenu dans la liste des mots fréquents
        for n in listmotsfrequents :
            if n in phrsplit :
                #Si il retrouve un mot de la liste des mots frequents alors il va ajouter à la valeur proba + 1 pour dire qu'il faut retenir cette phrase comme convenable
                proba += 1
        if proba > 0 :
            #Si la phrase est retenue alors on rajoute un peu de mise en forme
            codeprob = motdecode + " >>" + ' Avec une clé de : -'  + str(i) + " ou "  + str(26-i)
            #On ajoute cette phrase à une liste de phrases probables
            phrasesprobables.append(codeprob)

        #imprime le message avec la clé utilisé dans tout les cas
        print(motdecode, " : Avec comme clé : -",i, " ou ", 26-i)
    print ("------------------------------------------------------")
    #Affiche chaque phrase possible et sa clé
    for j in phrasesprobables :
        print("Phrase probable : << ", j)


#----------------------------------------------------------------------------------------
#programme principal
question = ""
while question != "c" and question != "b" and question != "d" :
    question = input("Voulez-vous coder un message, décoder un message ou trouver la clé d'un message codé ? Rentrez c, d ou b")
    question = question.lower()
if (question == "c" ) :
    message = input("Entrez un message à coder")
    clef = int(input("Entrez la clé de décalage"))
    print("Votre message codé : ", Cryptage(message, clef))
if (question == "d") :
    message = input("Entrez un message à décoder")
    clef = int(input("Entrez la clé de décalage"))
    print("Votre message décodé : ", Decryptage(message, clef))
if (question == "b") :
    message = input("Entrez un message à brute-forcer")
    print("Voici les possibles messages et leurs clés respectives : ")
    print("---------------------------------------------------------")
    BruteForce(message)













