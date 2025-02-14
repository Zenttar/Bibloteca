'Clase libreria'
class Estanteria:
    counter=0
    shelfs=[]
    def __init__(self, number, balda,balda_cap):
/*************  ✨ Codeium Command ⭐  *************/
        '''
        Constructor de la clase Estanteria, crea una estanteria con numero,
        balda y capacidad.
        
        Parameters
        ----------
        number : int
            Numero de la estanteria
        balda : int
            Numero de balda
        balda_cap : int
            Capacidad de la balda
        
        Returns
        -------
        None
        '''
/******  2cf0b42c-4376-4e9b-90cd-6bccd0e5c940  *******/
        self.number = number
        self.balda = balda
        self.balda_cap = balda_cap
        Estanteria.counter+=1

    def add_shelf(self):
        Estanteria.shelfs.append([self.number,self.balda,self.balda_cap])

    def check_shelf_cap(self):
        print('Hay capacidad')
