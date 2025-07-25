# Exercice 1
age = 20
print("Mon âge est:", age)

# Exercice 2
taille = 1.65
print("Ma taille est:", taille, "m")

# Exercice 3
nombre_complexe = 2 + 3j
print("Nombre complexe:", nombre_complexe)

# Exercice 4
base = float(input("Entrez la base: "))
hauteur = float(input("Entrez la hauteur: "))
aire = 0.5 * base * hauteur
print("La zone du triangle est:", aire)

# Exercice 5
a = float(input("Entrez le côté A: "))
b = float(input("Entrez le côté B: "))
c = float(input("Entrez le côté C: "))
perimetre = a + b + c
print("Le périmètre du triangle est:", perimetre)

# Exercice 6
longueur = float(input("Entrez la longueur: "))
largeur = float(input("Entrez la largeur: "))
surface = longueur * largeur
perimetre = 2 * (longueur + largeur)
print("Surface du rectangle:", surface)
print("Périmètre du rectangle:", perimetre)

# Exercice 7
rayon = float(input("Entrez le rayon: "))
pi = 3.14
aire = pi * rayon ** 2
circonference = 2 * pi * rayon
print("Aire du cercle:", aire)
print("Circonférence du cercle:", circonference)

# Exercice 8
pente = 2
print("La pente est:", pente)
x = 0
y = 2 * x - 2
print("Ordonnée à l'origine (quand x=0):", y)

# Exercice 9
x1, y1 = 2, 2
x2, y2 = 6, 10
pente_9 = (y2 - y1) / (x2 - x1)
print("Pente entre les deux points:", pente_9)
distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print("Distance euclidienne:", distance)

# Exercice 10
if pente == pente_9:
    print("Les deux pentes sont égales")
else:
    print("Les pentes sont différentes")

# Exercice 11
x = -3
y = x**2 + 6*x + 9
print("Pour x =", x, ", y =", y)

# Exercice 12
print(len("Python") != len("Dragon"))  # Falsy

# Exercice 13
print('on' in 'python' and 'on' in 'dragon')

# Exercice 14
phrase = "I hope this course is not full of jargon."
print('jargon' in phrase)

# Exercice 15
print('on' not in 'dragon' and 'on' not in 'python')

# Exercice 16
longueur = len('python')
float_longueur = float(longueur)
str_longueur = str(float_longueur)
print("Longueur:", longueur)
print("Float:", float_longueur)
print("String:", str_longueur)

# Exercice 17
nombre = int(input("Entrez un nombre: "))
if nombre % 2 == 0:
    print("Le nombre est pair")
else:
    print("Le nombre est impair")

# Exercice 18
print(7 // 3 == int(2.7))

# Exercice 19
print(type("10") == type(10))

# Exercice 20
try:
    print(int('9.8') == 10)
except:
    print("Erreur: '9.8' ne peut pas être converti en int directement")

# Exercice 21
heures = float(input("Entrez les heures: "))
taux = float(input("Entrez le taux par heure: "))
salaire = heures * taux
print("Votre gain hebdomadaire est:", salaire)

# Exercice 22
annees = int(input("Entrez le nombre d'années que vous avez vécu: "))
secondes = annees * 365 * 24 * 60 * 60
print("Vous vivez pendant", secondes, "secondes.")

# Exercice 23
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)
