import os 
da = int(input("Entrer dimension de liste A :  "))
a = []
for i in range(da) :
    a.append(int(input(f"Entrer la valeurs entière number {i+1} de la liste A :  ")))
os.system('cls' if os.name=='nt' else 'clear')

db = int(input("Entrer dimension de liste B :  "))
b = []
for i in range(db) :
    b.append(int(input(f"Entrer la valeurs entière number {i+1}  de la liste B :  ")))
os.system('cls' if os.name=='nt' else 'clear')    

print(f'A  =  {a}')
print(f'B  =  {b}')

aib = []    
for i in  a :
    for j in  b :
        if i == j :
            aib.append(i)
aib.sort()

aub = []
for i in a :
   aub.append(i)
for i in b :
   s = 0
   for j in a :
      if i != j :
         s=s+1
   if s == len(a) :
      aub.append(i)
aub.sort()

amb = []
for i in a :
   s=0
   for j in b :
      if i!=j :
         s=s+1
   if s == len(b) :
      amb.append(i)
amb.sort()

bma = []
for i in b :
   s=0
   for j in a :
      if i!=j :
         s=s+1
   if s == len(a) :
      bma.append(i)
bma.sort()

afb = []
for i in a :
     for j in b :
          afb.append(f"({i},{j})")

print(f"A unio B =  {aub}") 
print(f"A Intersection B =  {aib}")
print(f"A - B = {amb}")
print(f"B - A = {bma}")
print(f"Le produit cartésien de A et B est l'ensemble des points suivants  : \n {afb}")
print("\nprogram réalisé par yahya rhiba création personnel.....")
