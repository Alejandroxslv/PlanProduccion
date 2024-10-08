import time
import mysql.connector
from WorkOrder import WorkOrder, Prod_Show
import flet as ft

# [)>@06@0PN12204716-00@1MPFS32K146HFT0VLHR@2DT2420@3WO029663@4CUKOS@5MS3@6BP12034852@7BTQ25010@8CSE653F36Ah@9QT500@ALTQB32JG.000@BPONA@CMK12204716-00-ESW0067@DCNKostal@EJN12204716-00@FEPEPS MEXICO@@

if __name__ == '__main__':

    while True:
        print('---------------- MENU ----------------')
        print('1. Agregar batch a producción')
        print('2. Mostar material en Producción')
        print('3. Eliminar batch de producción')
        print('4. Mover batch de producción a PT')
        print('5. Mostrar material en PT')
        print('6. Dar salida a batch')
        print('0. Salir del programa')
        print('--------------------------------------')
        opt = input('Ingrese acción a realizar: ')
        if opt =='0':
            print('Saliendo')
            print('.')
            print('.')
            print('.')
            break
        elif opt=='1':
            print('Agregar batch a producción')
            lector = input('Trama de datos (DataMatrix): ')
            df = WorkOrder(lector)
            if df.isValid():
                if df.Prod_Exists():
                    print('Esta WorkOrder ya está en piso de producción')
                else:
                    df.Prod_Add()
                    print('Se agrega WorkOrder a piso de producción')
            else:
                print('Trama inválida. Por favor, ingrese una WO válida.')
        elif opt=='2':
            print('Mostrar producción')
            Prod_Show()
        elif opt=='3': #Eliminar de producción
            print('Eliminar batch de producción')
            lector = input('Trama de datos (DataMatrix): ')
            df = WorkOrder(lector)
            if df.isValid():
                if df.Prod_Exists():
                    df.Prod_Delete()
                    print('Se elimina WorkOrder de piso de producción')
                else:
                    print('Esta WorkOrder no existe en piso de producción')
            else:
                print('Trama inválida. Por favor, ingrese una WO válida.')
        elif opt=='4':
            print('Mover batch de producción a PT')
            lector = input('Trama de datos (DataMatrix): ')
            df = WorkOrder(lector)
            if df.Prod_Exists():
                df.PT_Add()
                print('Se agrega WorkOrder a PT')
                df.Prod_Delete()
                print('Se elimina WorkOrder de piso de producción')
            else:
                print('Esta WorkOrder no existe en piso de producción')
        elif opt=='5':
            print('Mostrar material en PT')

        elif opt=='6':
            lector = input('Trama de datos (DataMatrix): ')
            df = WorkOrder(lector)
            if df.PT_Exists():
                df.PT_Delete()
                print('Se elimina WorkOrder de PT')
            else:
                print('Esta WorkOrder no existe en PT')
