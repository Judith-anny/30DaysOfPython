EXERCICE2
print("Addition:", 3 + 4)           
print("Soustraction:", 3 - 4)       
print("Multiplication:", 3 * 4)     
print("Modulo:", 3 % 4)             
print("Division:", 3 / 4)           
print("Exponentielle:", 3 ** 4)     
print("Floor division:", 3 // 4)    # 0

# Affichage de chaînes (ton nom, prénom, pays, phrase)
print("Prénom: Judith")
print("Nom: Lama")
print("Pays: Allemagne")
print("Phrase: Je profite de 30 jours de python")

# Vérification des types de données
print("Type de 10:", type(10))  
print("Type de 9.8:", type(9.8))  
print("Type de 3.14:", type(3.14))  
print("Type de 4 - 4j:", type(4 - 4j))  
print("Type de liste:", type(['Asabeneh', 'Python', 'Finlande']))  
print("Type de prénom:", type("Judith"))  
print("Type de nom:", type("Lama"))  
print("Type de pays:", type("Allemagne"))  


EXERCICE3
# Exemples pour chaque type de données
x = 10                       
y = 3.14                     
z = 4-4j                   
nom = "Judith"               
est_vrai = True              
nombres = [1, 2, 3]          
coordonnees = (4, 5)         
unique = {1, 2, 3}           
personne = {'nom': 'Judith', 'age': 20}  

print("Exemple int:", x)
print("Exemple float:", y)
print("Exemple complex:", z)
print("Exemple string:", nom)
print("Exemple boolean:", est_vrai)
print("Exemple list:", nombres)
print("Exemple tuple:", coordonnees)
print("Exemple set:", unique)
print("Exemple dictionary:", personne)

# Calcul de la distance euclidienne entre (2,3) et (10,8)
import math

x1, y1 = 2, 3
x2, y2 = 10, 8

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Distance euclidienne entre (2,3) et (10,8):", distance)
