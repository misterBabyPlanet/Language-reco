


import string       # import de l'alphabet



def percent(texte):

    """ Renvoie les stats de pourcentage de présence de chaque lettre dans le texte sous forme d'un dictionnaire """

    def count_lettres(texte_string = texte):

        """ Renvoie un dictionnaire comportant des tuples (lettre : nb d'occurence de la lettre """

        dict_lettres = {}                                           # dictionnaire des lettres
        alphabet = string.ascii_lowercase                       # string comportant les lettres de l'alphabet en minuscule puis en majuscule

        for lettre in alphabet:                                     # pour chaque lettre de l'alphabet (mins puis majs)
            dict_lettres[lettre] = texte_string.count(lettre)           # on compte le nombre d'occurences et on ajoute le tuple au dictionnaire
        
        return dict_lettres                                         # on retourne le dictionnaire


    def count_to_percent(dictionnaire_lettres = count_lettres()):

        """ Transforme  les valeurs occurence de chaque tuple du dictionnaire en pourcentage"""

        def total(dict = dictionnaire_lettres):

            """ Retourne le total des occurences """

            total = 0                                                   # total

            for lettre, occur in dictionnaire_lettres.items():          # pour chaque lettre et nombre dans le tuple
                total += occur                                              #total est incrémenté du nombre d'occurences
        
            return total                                                # on retourne total
        
        total_lettres = total()                                     # on récupère le total des occurences         
        dict_percent = {}                                           # on créé le dictionnaire qui remplacera les occurences par leur pourcentage
        
        for lettre, occur in dictionnaire_lettres.items():          # pour chaque tuple
            dict_percent[lettre] = (occur / total_lettres) * 100        # on créé à dict_percent une valeur correspondant à la lettre avec le pourcentage des occurences
        
        return dict_percent                                         # on retourne le dictionnaire pourcentages
      

    return count_to_percent()       # renvoie le dictionnaire pourcentage