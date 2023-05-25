#RECETARIO
'''
Primero dara la bienvenida, informara la ruta de las recetas, y la cantidad de recetas que hay en esa ruta.
Luego dara las opciones al usuario:
                                                        1 Leer receta------------Elegir categoria
                                                                            |---------- Mostrar recetas
                                                                            |---- ------Elegir Receta
                                                        2 Crear receta---- -----Elegir Categoria
                                                                                |--------Elegir nombre
                                                                                |--------Escribir receta
                                                        3 Crear Categoria ----ELegir Nombre
                                                                                    |----Crear carpeta nueva en directorio
                                                        4 Eliminar Receta ------Elegir categoria
                                                                                  |----- Mostrar recetas
                                                                                  |----- Elegir Receta
                                                                                  |----- Borrar archivo
                                                        5 Eliminar Categoria--Elegir Categoria
                                                                                        |- Borrar Carpeta
                                                        6 Finalizar programa
                                                                                        |--- SALIR

'''
def raiz():
    from pathlib import Path
    print(Path.home())
    

def bienvenida():
    from pathlib import Path
    raiz= Path.home()
    recetas=Path(raiz,'Desktop\Programacion\Proyecto Dia_6-RECETARIO')
    print ("Bienvenido Chef!\n Las recetas estan en", recetas)
    print("\n")

def opciones():
   
    print('[1] Leer Receta')
    print('[2] Crear Receta')
    print('[3] Crear Categoría')
    print('[4] Eliminar Receta')
    print('[5] Eliminar Categoría')
    print('[6] Finalizar Programa')
    print('____________________')
    elije_op=int(input(">: "))

def categorias():
    print("[1] Carnes")
    print("[2] Pastas")
    print("[3] Ensaladas")
    print("[4] Postres")
    print("____________")
    elije_cat=int(input(">: "))

def programa(opciones,categorias):
     from pathlib import Path
     while elije_op !=6:
        if elije_op in range(1,7):
            if elije_op==1:
                categorias()
                if elije_cat==1:
                    print("Mostrando recetas de carnes")
                
                if leer in range(1,5):
                    if leer==1:
                        print('Mostrando recetas de Carnes') #Aqui mostraria las recetas.txt del directorio "Carnes"
                        opciones()
                    if leer==2:
                        print('Mostrando recetas de Pastas')#Aqui mostraria las recetas.txt del directorio "Pastas"
                        continue
                    if leer==3:
                        print('Mostrando recetas de Ensaladas')
                    if leer==4:
                        print('Mostrando recetas de Postres')

bienvenida()
opciones()
programa()
    
