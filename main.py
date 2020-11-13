import json
import glob
from collections import Counter


def percent(texte):
    """ 
    Renvoie un dictionnaire associant à chaque lettre sa densité, en pourcentage
    """
    dico_lettres = Counter(texte)
    total = sum(dico_lettres.values())                                    
    return {lettre: (occur/total)*100 for lettre, occur in dico_lettres.items()} 

def moyenne_diff(density, lang):

    density_diff = {}
    for lettre, valeur in density.items():
        if lettre in lang:
            density_diff[lettre] = abs(valeur - lang[lettre])

    return 100 - sum(density_diff.values()) / len(density_diff)


with open('dict_letters_repartition.json', 'r') as file:
    density_ref = json.load(file)


for filename in glob.glob("textes/*.txt"):
    print(f"\nTest avec le fichier '{filename}'")

    for lang in density_ref:
        with open(filename, 'r') as file:
            content = file.read()
        #stdev pour standard deviation
        stdev = moyenne_diff(percent(content), density_ref[lang]) 
        print(f"Match {lang} : {stdev}")