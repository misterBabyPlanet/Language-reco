import json
import glob
from collections import Counter


def density(text):
    """ 
    Renvoie un dictionnaire associant à chaque lettre sa densité, en pourcentage
    """
    text = tuple(filter(lambda c: 'A'<=c<='Z', map(str.upper, text)))                           
    return {l: (occur/len(text))*100 for l, occur in Counter(text).items()} 

def relative_diff(density, lang):

    density_diff = {}
    for char, valeur in density.items():
        if (char := char.upper()) in lang:
            density_diff[char] = abs(valeur-lang[char]) / lang[char] # écart relatif

    return sum(density_diff.values())


with open('dict_letters_repartition.json', 'r') as file:
    density_ref = json.load(file)


for filename in glob.glob("texts/*.txt"):
    print(f"\nTest avec le fichier '{filename}'")

    for lang, density_lang_ref in density_ref.items():
        with open(filename, 'r') as file:
            content = file.read()

        rel_diff = relative_diff(density(content), density_lang_ref) 
        print(f"Match {lang} : {100-rel_diff}")