class Voiture:
    def __init__(self,matricule,marque,couleur):
        self.matricule = matricule
        self.marque=marque
        self.couleur=couleur 



    def afficher_informations(self):
        print(f"les caracteristiques de cette voiture sont: matricule :{self.matricule},marque  :{self.marque},couleur: {self.couleur}")



class Parc:
    def __init__(self,id,adresse,capacite):
        self.id=id
        self.adresse=adresse
        self.capacite=capacite
        self.listeVoitures=[]     


    def entrerVoiture(self,voiture):
        if self.calculerNbrPlacesLibres() <=0:
            print(f"Impossible d'ajouter la voiture {voiture.matricule}:le parc est deja plein.")
            return   