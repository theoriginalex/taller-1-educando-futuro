import os
from colorama import init, Fore
from _1periodo import CrudPeriodos
from _2nivel_educativo import CrudNivelesEducativos
from _3asignaturas import CrudAsignaturas
from _4profesor import CrudProfesores
from _5estudiante import CrudEstudiantes
from _6nota import CrudNotas
from _7detalle_nota import CrudDetalleNotas

# Inicializar colorama
init(autoreset=True)

crud_periodos = CrudPeriodos("archivos/periodos.json")
crud_niveles = CrudNivelesEducativos("archivos/niveles.json")
crud_asignaturas = CrudAsignaturas("archivos/asignaturas.json")
crud_profesores = CrudProfesores("archivos/profesores.json")
crud_estudiantes = CrudEstudiantes("archivos/estudiantes.json")
crud_notas = CrudNotas("archivos/notas.json")
crud_detalle_notas = CrudDetalleNotas("archivos/detalles_notas.json")

# Función para simular limpiar la pantalla
def borrarPantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Clase Menu para mostrar un menú en pantalla
class Menu:
    def __init__(self, titulo, opciones, x=20, y=10):
        self.titulo = titulo
        self.opciones = opciones
        self.x = x
        self.y = y

    def menu(self):
        print(Fore.CYAN + f"{self.titulo.center(50, '=')}")
        for opcion in self.opciones:
            print(Fore.GREEN + opcion)
        print(Fore.CYAN + "="*50)
        opc = input(Fore.YELLOW + "Seleccione una opción: ")
        return opc

# Menu Principal del sistema "Educando Futuro"
opc = ''
while opc != '8':
    borrarPantalla()
    menu_main = Menu( "Menu Educando Futuro", [
        Fore.GREEN + "1) Periodos Académicos",
        Fore.GREEN + "2) Niveles Educativos",
        Fore.GREEN + "3) Asignaturas",
        Fore.GREEN + "4) Profesores",
        Fore.GREEN + "5) Estudiantes",
        Fore.GREEN + "6) Notas",
        Fore.GREEN + "7) Detalle de Notas",
        Fore.RED + "8) Salir"
    ])

    opc = menu_main.menu()

    # Menú de Periodos Académicos
    if opc == "1":
        opc1 = ''
        while opc1 != '5':
            borrarPantalla()
            menu_periodos = Menu("Menu Periodos Académicos", [
                Fore.GREEN + "1) Ingresar",
                Fore.GREEN + "2) Actualizar",
                Fore.GREEN + "3) Eliminar",
                Fore.GREEN + "4) Consultar",
                Fore.GREEN + "5) Salir"
            ])
            opc1 = menu_periodos.menu()
            if opc1 == "1":
                crud_periodos.create()
            elif opc1 == "2":
                crud_periodos.update()
            elif opc1 == "3":
                crud_periodos.delete()
            elif opc1 == "4":
                crud_periodos.consult()
            print(Fore.YELLOW + "Regresando al menu Periodos Académicos...")

    # Menú de Niveles Educativos
    elif opc == "2":
        opc2 = ''
        while opc2 != '5':
            borrarPantalla()
            menu_niveles = Menu("Menu Niveles Educativos", [
                Fore.GREEN + "1) Ingresar",
                Fore.GREEN + "2) Actualizar",
                Fore.GREEN + "3) Eliminar",
                Fore.GREEN + "4) Consultar",
                Fore.RED + "5) Salir"
            ])
            opc2 = menu_niveles.menu()
            if opc2 == "1":
                crud_niveles.create()
            elif opc2 == "2":
                crud_niveles.update()
            elif opc2 == "3":
                crud_niveles.delete()
            elif opc2 == "4":
                crud_niveles.consult()
            print(Fore.YELLOW + "Regresando al menu Niveles Educativos...")

    # Menú de Asignaturas
    elif opc == "3":
        opc3 = ''
        while opc3 != '5':
            borrarPantalla()
            menu_asignaturas = Menu("Menu Asignaturas", [
                Fore.GREEN + "1) Ingresar",
                Fore.GREEN + "2) Actualizar",
                Fore.GREEN + "3) Eliminar",
                Fore.GREEN + "4) Consultar",
                Fore.RED + "5) Salir"
            ])
            opc3 = menu_asignaturas.menu()
            if opc3 == "1":
                crud_asignaturas.create()
            elif opc3 == "2":
                crud_asignaturas.update()
            elif opc3 == "3":
                crud_asignaturas.delete()
            elif opc3 == "4":
                crud_asignaturas.consult()
            print(Fore.YELLOW + "Regresando al menu Asignaturas...")

    # Menú de Profesores
    elif opc == "4":
        opc4 = ''
        while opc4 != '5':
            borrarPantalla()
            menu_profesores = Menu("Menu Profesores", [
                Fore.GREEN + "1) Ingresar",
                Fore.GREEN + "2) Actualizar",
                Fore.GREEN + "3) Eliminar",
                Fore.GREEN + "4) Consultar",
                Fore.RED + "5) Salir"
            ])
            opc4 = menu_profesores.menu()
            if opc4 == "1":
                crud_profesores.create()
            elif opc4 == "2":
                crud_profesores.update()
            elif opc4 == "3":
                crud_profesores.delete()
            elif opc4 == "4":
                crud_profesores.consult()
            print(Fore.YELLOW + "Regresando al menu Profesores...")

    # Menú de Estudiantes
    elif opc == "5":
        opc5 = ''
        while opc5 != '5':
            borrarPantalla()
            menu_estudiantes = Menu("Menu Estudiantes", [
                Fore.GREEN + "1) Ingresar",
                Fore.GREEN + "2) Actualizar",
                Fore.GREEN + "3) Eliminar",
                Fore.GREEN + "4) Consultar",
                Fore.RED + "5) Salir"
            ])
            opc5 = menu_estudiantes.menu()
            if opc5 == "1":
                crud_estudiantes.create()
            elif opc5 == "2":
                crud_estudiantes.update()
            elif opc5 == "3":
                crud_estudiantes.delete()
            elif opc5 == "4":
                crud_estudiantes.consult()
            print(Fore.YELLOW + "Regresando al menu Estudiantes...")

    # Menú de Notas
    elif opc == "6":
        opc6 = ''
        while opc6 != '5':
            borrarPantalla()
            menu_notas = Menu("Menu Notas", [
                Fore.GREEN + "1) Ingresar",
                Fore.GREEN + "2) Actualizar",
                Fore.GREEN + "3) Eliminar",
                Fore.GREEN + "4) Consultar",
                Fore.RED + "5) Salir"
            ])
            opc6 = menu_notas.menu()
            if opc6 == "1":
                crud_notas.create()
            elif opc6 == "2":
                crud_notas.update()
            elif opc6 == "3":
                crud_notas.delete()
            elif opc6 == "4":
                crud_notas.consult()
            print(Fore.YELLOW + "Regresando al menu Notas...")

    # Menú de Detalle de Notas
    elif opc == "7":
        opc7 = ''
        while opc7 != '5':
            borrarPantalla()
            menu_detalle_notas = Menu("Menu Detalle de Notas", [
                Fore.GREEN + "1) Ingresar",
                Fore.GREEN + "2) Actualizar",
                Fore.GREEN + "3) Eliminar",
                Fore.GREEN + "4) Consultar",
                Fore.RED + "5) Salir"
            ])
            opc7 = menu_detalle_notas.menu()
            if opc7 == "1":
                crud_detalle_notas.create()
            elif opc7 == "2":
                crud_detalle_notas.update()
            elif opc7 == "3":
                crud_detalle_notas.delete()
            elif opc7 == "4":
                crud_detalle_notas.consult()
            print(Fore.YELLOW + "Regresando al menu Detalle de Notas...")

    print(Fore.YELLOW + "Regresando al menu Principal...")

borrarPantalla()
input(Fore.CYAN + "Presione una tecla para salir...")
borrarPantalla()
