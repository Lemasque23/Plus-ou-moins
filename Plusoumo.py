import random
C=1
D=2

while D==2:
  E=0
  B=random.randrange(-1000000,1000000)
  while C==1:  
    print("Choisis un")
    A=int(input("nombre : "))
    if A>B:
      print("Trop grand !")
      print("    ")
      E=E+1
    if A<B:
      print("Trop petit")
      print("   ")
      E=E+1
    if A==B:
      print("Gagne")
      E=E+1
      print("en ",E," coups")
      C=2
  print("1 Pour quitter")
  print("2 Pour recommencer")
  D=int(input("Puis EXE : "))  
  if D==2:
    C=1
    
          