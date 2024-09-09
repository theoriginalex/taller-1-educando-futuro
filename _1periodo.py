from datetime import date
from clsJson import JsonFile
from iCrud import ICrud


class Periodos:
    def __init__(self, id_periodo, nombre, active=True, fecha_creacion=None):
        self.id_periodo = id_periodo
        self.nombre = nombre
        self.fecha_creacion = fecha_creacion if fecha_creacion else date.today()
        self.active = active

    def to_dict(self):
        return {
            'id_periodo': self.id_periodo,
            'nombre': self.nombre,
            'fecha_creacion': str(self.fecha_creacion),
            'active': 'Activo' if self.active else 'Inactivo'
        }


class CrudPeriodos(ICrud):
    def __init__(self, json_file):
        self.file_manager = JsonFile(json_file)

    def _get_next_id(self):
        """ Obtiene el próximo ID basado en el último periodo registrado """
        data = self.file_manager.read()
        if data:
            last_id = data[-1]['id_periodo']  # Toma el último ID
            return last_id + 1  # Retorna el siguiente ID
        return 1  # Si no hay datos, comienza con 1

    def create(self):
        nombre = input("Ingrese el nombre del periodo: ")
        active = input("¿El periodo está activo? (S/N): ").lower() == 's'

        # Generar el nuevo ID automáticamente
        id_periodo = self._get_next_id()

        # Crear nuevo periodo
        periodo = Periodos(id_periodo, nombre, active)

        # Guardar en archivo JSON
        data = self.file_manager.read()
        data.append(periodo.to_dict())
        self.file_manager.save(data)
        print(f"Periodo registrado exitosamente con ID: {id_periodo}.")

    def update(self):
        id_periodo = input("Ingrese el ID del periodo a actualizar: ")
        periodos = self.file_manager.find("id_periodo", int(id_periodo))
        if periodos:
            periodo = periodos[0]
            periodo["nombre"] = input(f"Nombre actual ({periodo['nombre']}): ") or periodo["nombre"]
            active_input = input(f"Estado actual ({'Activo' if periodo['active'] == 'Activo' else 'Inactivo'}): (S/N) ")
            if active_input:
                periodo["active"] = 'Activo' if active_input.lower() == 's' else 'Inactivo'

            data = self.file_manager.read()
            for i, p in enumerate(data):
                if p['id_periodo'] == int(id_periodo):
                    data[i] = periodo
                    break
            self.file_manager.save(data)
            print("Periodo actualizado exitosamente.")
        else:
            print("Periodo no encontrado.")

    def delete(self):
        id_periodo = input("Ingrese el ID del periodo a eliminar: ")
        data = self.file_manager.read()
        data = [p for p in data if p['id_periodo'] != int(id_periodo)]
        self.file_manager.save(data)
        print("Periodo eliminado exitosamente.")


    def consult(self):
        id_periodo = input("Ingrese el ID del periodo a consultar: ")
        periodos = self.file_manager.find("id_periodo", int(id_periodo))
        if periodos:
            print(f"Periodo encontrado: {periodos[0]}")
        else:
            print("Periodo no encontrado.")
