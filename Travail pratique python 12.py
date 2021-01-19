import os 
A = []
B = []
print("bonjour....Entrer les elements de la matrice A  à deux dimensions de taille 3x3  ")
print("""soit les position comme sa :
               | A[0][0]   A[0][1]    A[0][2] |
               | A[1][0]   A[1][1]    A[1][2] |
               | A[2][0]   A[2][1]    A[2][2] |                    \n""")

for i in range(3) :
    a=[]
    for j in range(3) :
        j = int(input(f"entrer A[{i}][{j}] : "))
        a.append(j)
    A.append(a)
os.system('cls' if os.name=='nt' else 'clear')

print("Entrer les elements de la matrice B  à deux dimensions de taille 3x3  ")
print("""soit les position comme sa :
               | B[0][0]   B[0][1]    B[0][2] |
               | B[1][0]   B[1][1]    B[1][2] |
               | B[2][0]   B[2][1]    B[2][2] |                   \n""")

for i in range(3) :
    b=[]
    for j in range(3) :
        j = int(input(f"entrer B[{i}][{j}] : "))
        b.append(j)
    B.append(b)
os.system('cls' if os.name=='nt' else 'clear')

print("\t\t\tla matrice A : ")
for i in range(3) :
    for j in range(3) :
        print(f"{A[i][j]}   ",end=" ")
    print()

print("\n\t\t\tla matrice B : ")
for i in range(3) :
    for j in range( 3) :
        print(f"{B[i][j]}   ",end=" ")
    print() 

na=len(A) 
ma=len(A[0]) 
nb=len(B) 
mb=len(B[0])


s = [[A[i][j] + B[i][j] for j in range(ma)] for i in range(na)]
print("\n\t\t\tla matrice  A+B : ")
for i in range(3) :
    for j in range(3) :
        print(f"{s[i][j]}   ",end=" ")
    print()


h =  [[A[i][j] - B[i][j] for j in range(ma)] for i in range(na)]

print("\n\t\t\tla matrice  A-B : ")
for i in range(3) :
    for j in range(3) :
        print(f"{h[i][j]}   ",end=" ")
    print()


f = [[0]*ma for i in range(na)]
for i in range(na):
    for j in range(ma):
        for k in range(nb):
            f[i][j] += A[i][k] * B[k][j]

print("\n\t\t\tla matrice  A*B : ")
for i in range(3) :
    for j in range(3) :
        print(f"{f[i][j]}   ",end=" ")
    print()                


va  = [[0]*ma for i in range(na)] 
for i in range(na):
     for j in range(ma):
         va[j][i]= A[i][j]

print("\n\t\t\tTransposée de A : ")
for i in range(3) :
    for j in range(3) :
        print(f"{va[i][j]}   ",end=" ")
    print()


vb  = [[0]*mb for i in range(nb)] 
for i in range(nb):
     for j in range(mb):
         vb[j][i]= B[i][j]

print("\n\t\t\tTransposée de B : ")
for i in range(3) :
    for j in range(3) :
        print(f"{vb[i][j]}   ",end=" ")
    print()

for i in range(3) :
    for j in range(3) :
        detA = A[0][0]*((A[1][1]*A[2][2])-(A[2][1]*A[1][2]))-A[0][1]*((A[1][0]*A[2][2])-(A[2][0]*A[1][2]))+A[0][2]*((A[1][0]*A[2][1])-(A[2][0]*A[1][1]))    

print("\n\tLe déterminant de la matrice A =  ",detA)

for i in range(3) :
    for j in range(3) :
        detB = B[0][0]*((B[1][1]*B[2][2])-(B[2][1]*B[1][2]))-B[0][1]*((B[1][0]*B[2][2])-(B[2][0]*B[1][2]))+B[0][2]*((B[1][0]*B[2][1])-(B[2][0]*B[1][1]))    

print(f"\n\tLe déterminant de la matrice B =  {detB} \n")
