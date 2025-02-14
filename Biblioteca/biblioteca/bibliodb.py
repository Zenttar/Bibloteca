import sqlite3

class BiblioDB:
    # def connect_db():
    #     db=sqlite3.connect("biblio.db")
    # def close_db(db):
    #    db.close()   

        
#estanterías    
    def add_lib_shelf():
        print('add shelf')

    def mod_lib_shelf():
        print('mod shelf')

    def del_lib_shelf():
        print('mod shelf')

    def check_cap_balda():
        print('mod shelf')

#libros
    def add_lib_book(number,name,year,shelf,index):
        print('add book')
        db=sqlite3.connect("biblio.db")
        cur=db.cursor()
        cur.execute("INSERT INTO LIBROS VALUES (?,?,?,?,?",number,name,year,shelf,index)
        db.commit()
        db.close()
        #libro=Libreria.Libreria(book_name,book_year,book_shelf,book_number,book_index)
    def mod_lib_book():
        print('add book')
    def del_lib_book():
        print('del book')