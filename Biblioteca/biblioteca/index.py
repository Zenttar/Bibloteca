import utils
import utilsShelf

user_lib_create_or_exist=input('1-Empezar con una nueva librería.\n2-continuar con una existente.\nElija una de las opciones:\n')
if user_lib_create_or_exist=='1':
    while user_lib_create_or_exist == '1':
        user_input2=input('Para añadir una estantería, pulse 1\n, para ver la capacidad existente, pulse 2\n, para eliminar una estantería, pulse 3 ')
        
        if user_input2=='1':
            utilsShelf.add_shelf()
        
        elif user_input2=='2':
            utilsShelf.check_capacity_shelf()
        
        elif user_input2=='3':
            utilsShelf.delete_shelf()
        
        else:
            break

elif user_lib_create_or_exist=='2':
    while user_lib_create_or_exist == '2':
        user_input2=input('Para añadir un nuevo libro, pulse 1\n, para ver los libros existentes, pulse 2\n, para borrar un libro, pulse 3 ')
        
        if user_input2=='1':
            print('Ha pulsado 1, añadir libro')

            utils.add_book_to_library()

        elif user_input2=='2':
            print('ha pulsado 2, ver libros existentes')
            utils.view_list_of_books()

        elif user_input2=='3':
            print('Ha pulsado la opcion 3, borrar libro')
            utils.delete_book()

        else:
            break