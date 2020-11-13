
import os

from stats.stat_count import percent as percent_text
from stats.stat_gen import moyenne_diff
from stats import dict_valeurs_types_lettres


def contenu_file(path):

    with open(path, 'r') as file:
        return file.read()


liste_files = os.listdir("./textes")

for fichier in liste_files:
    print(f"test avec le fichier '{fichier}'")
    print('')
    print("match FR : ", moyenne_diff(percent_text(contenu_file(f"./textes/{fichier}")), dict_valeurs_types_lettres.Francais))
    print("match EN : ", moyenne_diff(percent_text(contenu_file(f"./textes/{fichier}")), dict_valeurs_types_lettres.Anglais))
    print("match LA : ", moyenne_diff(percent_text(contenu_file(f"./textes/{fichier}")), dict_valeurs_types_lettres.Latin))
    print('')
    print('---')
    print('')

