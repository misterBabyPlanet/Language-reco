

def moyenne_diff(liste, langue):

    def liste_diff(liste = liste, langue = langue):

        def diff(numb1, numb2):
            return abs(numb2 - numb1)
        
        liste_dif = {}

        for lettre, valeur in liste.items():

            if lettre in langue:
                liste_dif[lettre] = diff(valeur, langue[lettre])

        return liste_dif


    def moyenne():
        
        liste = liste_diff()
        return sum(liste.values()) / len(liste)
    

    def pourcentage(diff_pourc = moyenne()):

        return 100 - diff_pourc
    
    
    return pourcentage()
