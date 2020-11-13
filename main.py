import glob
import json
from collections import Counter


def density(text):
    """
    Renvoie un dictionnaire associant à chaque lettre sa densité, en pourcentage
    """
    text = tuple(filter(lambda c: "A" <= c <= "Z", map(str.upper, text)))
    return {
        letter: (occur / len(text)) * 100 for letter, occur in Counter(text).items()
    }


def diff(density, lang):

    density_diff = {}
    for char, valeur in density.items():
        if (char := char.upper()) in lang:
            density_diff[char] = abs(valeur - lang[char])

    return sum(density_diff.values())


with open("dict_letters_repartition.json") as file:
    density_ref = json.load(file)


for filename in glob.glob("texts/*.txt"):
    print(f"\nTest avec le fichier '{filename}'")

    for lang, density_lang_ref in density_ref.items():
        with open(filename) as file:
            content = file.read()

        rel_diff = diff(density(content), density_lang_ref)
        print(f"Match {lang} : {(100 - rel_diff):.2f}%")
