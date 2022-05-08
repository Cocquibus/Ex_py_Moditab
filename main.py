#modification tableau
import random
monTab = ["fraise","pomme","cerise","melon","citron"]
del monTab[0]
print(monTab)
print(len(monTab))
#ajoute un élément en dernier
monTab.append("dernierElement")
print(monTab)
#ajoute un élément a l'index choisi
monTab.insert(0,"premierElement")
print(monTab)
#met un élément en majuscule
monTab[1] = monTab[1].upper()
print(monTab)
#permet de mélanger un tableau
print(random.sample(monTab,(len(monTab))))
chiffres = [4, 5, 2, 1, 3]
print(chiffres)
#mettre en croissant la liste
chiffres = sorted(chiffres)
print(chiffres)
#reverse le mode croissant
chiffres = sorted(chiffres, reverse=True)
print(chiffres, type(chiffres), chiffres[0], type(chiffres[0]))
#boucle qui permet de modifier chaque élement en string
a = 0
for i in chiffres:
    i = str(i)
    chiffres[a] = i
    print(type(i), i)
    a =+ 1
print(chiffres, type(chiffres), chiffres[0], type(chiffres[0]))