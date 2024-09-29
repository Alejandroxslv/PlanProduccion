import time
import mysql.connector
from WorkOrder import WorkOrder
import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

# [)>@06@0PN12204716-00@1MPFS32K146HFT0VLHR@2DT2420@3WO029663@4CUKOS@5MS3@6BP12034852@7BTQ25010@8CSE653F36Ah@9QT500@ALTQB32JG.000@BPONA@CMK12204716-00-ESW0067@DCNKostal@EJN12204716-00@FEPEPS MEXICO@@
if __name__ == '__main__':
    ft.app(main)

    # while True:
    #     print('---------------- MENU ----------------')
    #     print('1. Agregar a producción')
    #     print('2. Quitar de producción')
    #     print('3. Mover a PT')
    #     print('4. Dar salida')
    #     print('0. Salir')
    #     print('--------------------------------------')
    #     opt = input('Ingrese acción a realizar: ')
    #     if opt =='0':
    #         break
    #     elif opt=='1':
    #         lector = input('Trama de datos (DataMatrix): ')
    #         df = WorkOrder(lector)
    #         if df.isValid():
    #             if df.Prod_Exists():
    #                 print('Esta WorkOrder ya está en piso de producción')
    #             else:
    #                 df.Prod_Add()
    #                 print('Se agrega WorkOrder a piso de producción')
    #         else:
    #             print('Trama inválida. Por favor, ingrese una WO válida.')
    #     elif opt=='2':
    #         lector = input('Trama de datos (DataMatrix): ')
    #         df = WorkOrder(lector)
    #         if df.isValid():
    #             if df.Prod_Exists():
    #                 df.Prod_Delete()
    #                 print('Se elimina WorkOrder de piso de producción')
    #             else:
    #                 print('Esta WorkOrder no existe en piso de producción')
    #         else:
    #             print('Trama inválida. Por favor, ingrese una WO válida.')
    #     elif opt=='3':
    #         lector = input('Trama de datos (DataMatrix): ')
    #         df = WorkOrder(lector)
    #         if df.Prod_Exists():
    #             df.PT_Add()
    #             print('Se agrega WorkOrder a PT')
    #             df.Prod_Delete()
    #             print('Se elimina WorkOrder de piso de producción')
    #         else:
    #             print('Esta WorkOrder no existe en piso de producción')
    #     elif opt=='4':
    #         lector = input('Trama de datos (DataMatrix): ')
    #         df = WorkOrder(lector)
    #         if df.PT_Exists():
    #             df.PT_Delete()
    #             print('Se elimina WorkOrder de PT')
    #         else:
    #             print('Esta WorkOrder no existe en PT')






