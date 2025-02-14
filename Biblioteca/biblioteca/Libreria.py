'Clase libreria'

class Libreria:
    counter=0
    libros=[]
    def __init__(self, name, year,shelf,number,index):
        self.name = name
        self.year = year
        self.shelf = shelf
        self.number = number
        self.index = index
        Libreria.counter+=1

    def new_book(self):
        
        return f"Hi, The new book have the following data: name: {self.name} published on {self.year} and this book is in {self.shelf} with number {self.number}"
        
    def add_book(self):
        Libreria.libros.append([self.index,self.name,self.year,self.shelf,self.number])

    def list_book():
        for i in Libreria.libros:
            print(f'Nombre: {i[1]}, Año de publicación: {i[2]}, estantería: {i[3]}, número de libro {i[4]} e indice: {i[0]}')

    def delete_book(index):
        for i in Libreria.libros:
            print(i[4])
            if i[4]==index:
                user_input_del=input(f'Se va a borrar el libro con índice {index}\nBorrar? Y/N')
                if user_input_del=='Y':
                    Libreria.libros.remove(i)
                    print('Se ha borrado correctamente el libro')

    @classmethod
    def create_anonymous(cls):
        return Libreria('No book', 1800, 0, 0)
    
   