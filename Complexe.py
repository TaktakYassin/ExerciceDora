from cmath import *

class Complexe(object):
    #definition de la méthode aui permet de créer les nombres complexes
    def __init__(self,a=0.0,b=0.0):
        self.real=float(a)
        self.imag=float(b)

    # Renvoie une chaîne contenant une représentation imprimable d'un objet
    def __repr__(self):
        return(str(self.real)+'+'+str(self.imag)+'i')

    # surcharge de l'opérateur -
    def __sub__(self,autreComplex):
        return Complexe(self.real-autreComplex.real,self.imag-autreComplex.imag)
    #surcharge de l'opérateur *
    def __mul__(self,autreComplex):
        x = self.real*autreComplex.real-self.imag*autreComplex.imag
        y = self.real*autreComplex.imag+self.imag*autreComplex.real
        return Complexe(x,y)
    def __truediv__(self,autreComplex):
        denominateur=autreComplex.real*autreComplex.real+autreComplex.imag*autreComplex.imag
        multiplicationResult = self*(Complexe(autreComplex.real,-autreComplex.imag))
        return Complexe(multiplicationResult.real/denominateur,multiplicationResult.real/denominateur)

a=Complexe(1,2)
print(a)
b=a*a
print(b)
c=a/a
print(c)
