'Clase libreria'
class Estanteria:
    counter=0
    shelfs=[]
    def __init__(self, number, balda,balda_cap):
        self.number = number
        self.balda = balda
        self.balda_cap = balda_cap
        Estanteria.counter+=1

    def add_shelf(self):
        Estanteria.shelfs.append([self.number,self.balda,self.balda_cap])

    def check_shelf_cap(self):
        print('Hay capacidad')
