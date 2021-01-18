def agee(nome) :
     age = 0
     while age  ==  0:    
         try :
             age_str = input(nome +" quel est votre age ? ")
             age = int(age_str)
         except :
            print("Erreur try again ")
     return age 


def nombres_de_personne() :
     a = 0
     while a  ==  0:    
         try :
             a_str = input(" combien de personnes es-tu ? ")
             a = int(a_str)
         except :
            print("Erreur try again ")
     return a 


def nomm(number) :
     nom = ""
     while nom == "" :
         nom = input(f" entrer le  nom de personne number {number} ? ")
     return nom


def ecrire(n,a) :
     print("vous  appelez "+ n +" et vous avez ", a , " ans , ",end=" ")
     if a < 18 :
         print("et vous etez mineur")
     else :
         print("et vous etez majeur")

#main :    
nombres_de_personne = nombres_de_personne() 
for i in range (nombres_de_personne) :
     nom = nomm(i+1)
     age = agee(nom)
     ecrire(nom,age)
