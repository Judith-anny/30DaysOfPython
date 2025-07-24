# Jour 2: 30 Days of Python Programming

# Déclarations de variables
first_name = "Judith"
last_name = "Lama"
full_name = first_name + " " + last_name
country = "Togo"
city = "Lome"
age = 20
year = 2025
is_married = False
is_true = True
is_light_on = True

# Déclaration multiple sur une seule ligne
x, y, z = 1, 2, 3

# Vérification des types
print("Types des variables :")
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

#  Longueur du prénom
print("Longueur du prénom :", len(first_name))

# Comparaison longueur prénom vs nom de famille
print("Prénom et nom ont la même longueur :", len(first_name) == len(last_name))
print("Prénom plus long que nom :", len(first_name) > len(last_name))
print("Prénom plus court que nom :", len(first_name) < len(last_name))

# Opérations mathématiques
num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
floor_division = num_one // num_two

print("Somme :", total)
print("Différence :", diff)
print("Produit :", product)
print("Division :", division)
print("Reste :", remainder)
print("Floor Division :", floor_division)

# Calculs sur un cercle
import math

radius = 30
area_of_circle = math.pi * radius ** 2
circum_of_circle = 2 * math.pi * radius

print("Aire du cercle :", area_of_circle)
print("Circonférence du cercle :", circum_of_circle)

# Aire avec entrée utilisateur
radius = float(input("Entrez le rayon du cercle : "))
area = math.pi * radius ** 2
print("L'aire du cercle est :", area)

# Input utilisateur pour infos personnelles
first_name = input("Quel est votre prénom ? ")
last_name = input("Quel est votre nom de famille ? ")
country = input("Votre pays ? ")
age = input("Votre âge ? ")

print("Informations utilisateur :", first_name, last_name, country, age)

# Mots clés réservés Python
help("keywords")
