#RECETARIO

def bienvenida():
    from pathlib import Path
    ruta= Path.home()
    ruta_recetas =  Path(ruta,'Python\Proyectos\Proyecto Dia_6-RECETARIO')
    print ("Bienvenido Chef! Las recetas estan en", ruta_recetas)

def opciones():
   
    print('[1] Leer Receta')
    print('[2] Crear Receta')
    print('[3] Crear Categoría')
    print('[4] Eliminar Receta')
    print('[5] Eliminar Categoría')
    print('[6] Finalizar Programa')
    print('____________________')
  

def eleccion(opciones):
     from pathlib import Path
     ruta=Path.home()
     ruta_recetas =  Path(ruta,'Python\Proyectos\Proyecto Dia_6-RECETARIO')
     ruta_carnes= Path(ruta_recetas,'Carnes')
     ruta_ensaladas=0
     ruta_postres=0
     ruta_pastas=0
     opcion_elegida= int(input('Ingresa una opcion: '))
     if opcion_elegida in range(1,7):
        if opcion_elegida==1:
            print('[1] Carne')
            print('[2] Pastas')
            print('[3] Ensaladas')
            print('[4] Postres')
            leer=int(input('Elija Categoria: '))
            if leer in range(1,5):
                if leer==1:
                    print('Mostrando recetas de Carnes')
                    
                if leer==2:
                    print('Mostrando recetas de Pastas')
                    
                if leer==3:
                    print('Mostrando recetas de Ensaladas')
                    
                if leer==4:
                    print('Mostrando recetas de Postres')
                    
     print('Opcion erronea')
     return opciones()

import os
opciones()
eleccion(opciones)

        
    


    


    












#FUNCIONES DEL PROGRAMA

'''
1) Leer receta
2) Crear Receta
3) Crear Categoría
4) Eliminar Receta
5) Eliminar Categoría
6) Finalizar Programa
'''

#opcion=input("Ingresa una opción: ")

