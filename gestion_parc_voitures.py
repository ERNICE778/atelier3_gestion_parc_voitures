class Voiture:
    def __init__(self,matricule,marque,couleur):
        self.matricule = matricule
        self.marque=marque
        self.couleur=couleur 



    def afficher_informations(self):
        print(f"les caracteristiques de cette voiture sont: matricule :{self.matricule},marque  :{self.marque},couleur: {self.couleur}")