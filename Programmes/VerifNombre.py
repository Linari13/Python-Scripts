def VerifNombreDansPlage (Entree,Mini=0,Maxi=100):

  NumOk = False
  
  while NumOk == False:
    if Entree.isdigit()== False:
      Entree = input ('Ceci n\'est pas un nombre entier, réessayez : ')
    elif Mini>int(Entree) or int(Entree)>Maxi:
      Entree = input(f"le chiffre doit être compris entre {Mini} et {Maxi}, réessayez : ")
    else:
      NumOk = True

  return int(Entree)

  if __name__ == "__main__":
        VerifNombreDansPlage()