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
        
        presence_vehicule = False
        for  v in self.listeVoitures:
            if v.matricule == voiture.matricule:
                presence_vehicule = True
                break

        if presence_vehicule :
            print (f"la voiture {voiture.matricule} est deja danc le parc .")
        else :
            self.listeVoitures.append(voiture)
            print(f"voiture ajoutee avec succes: la voiture {voiture.matricule} est entree dans le parc")
        

    def sortirVoiture(self,voiture):
        retraitVoiture = None
        for v in self.listeVoitures:
            if v.matricule == voiture.matricule:
                retraitVoiture = v
                break
        if retraitVoiture:
            self.listeVoitures.remove(retraitVoiture)    
            print(f"la voiture {voiture.matricule} est sortie avec success")
        else :
            print (f"la voiture {voiture.matricule} n'est pas presente dans le parc")       


    
    def calculerNbrPlacesLibres(self):
        return self.capacite -len(self.listeVoitures)    


parc_boreal = Parc(1,"60 Distillery",3)


