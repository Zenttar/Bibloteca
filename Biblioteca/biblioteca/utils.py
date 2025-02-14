import Libreria

def add_book_to_library():
    book_name=input('Inserte nombre del libro: \n')
    book_year=input('Inserte año del libro: \n')
    book_shelf=input('Inserte estantería del libro: \n')
    book_number=input('Inserte número del libro: \n')
    book_index=input('Inserte índice único del libro: \n')
    libro=Libreria.Libreria(book_name,book_year,book_shelf,book_number,book_index)
    libro.new_book()
    libro.add_book()

    print(f'Se va a añadir el siguiente libro: {book_name}')
    
def view_list_of_books():
    print(Libreria.Libreria.list_book())

def delete_book():
    user_del=input('Inserte el índice del libro a borrar: \n')
    Libreria.Libreria.delete_book(user_del)