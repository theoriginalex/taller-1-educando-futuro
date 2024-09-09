from datetime import date
from clsJson import JsonFile
from iCrud import ICrud


class Estudiante:
    def __init__(self, id, nombre, active=True, fecha_creacion=None):
        self.id = id
        self.nombre = nombre
        self.fecha_creacion = fecha_creacion if fecha_creacion else date.today()
        self.estado = "Activo" if active else "Inactivo"

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'fecha_creacion': str(self.fecha_creacion),
            'estado': self.estado
        }


class CrudEstudiantes(ICrud):
    def __init__(self, json_file):
        self.file_manager = JsonFile(json_file)

    def _get_next_id(self):
        """ Obtiene el próximo ID basado en el último estudiante registrado """
        data = self.file_manager.read()
        if data:
            last_id = data[-1]['id']  # Toma el último ID
            return last_id + 1  # Retorna el siguiente ID
        return 1  # Si no hay datos, comienza con 1

    def create(self):
        nombre = input("Ingrese el nombre del estudiante: ")
        active = input("¿El estudiante está activo? (S/N): ").lower() == 's'

        # Generar el nuevo ID automáticamente
        id_estudiante = self._get_next_id()

        # Crear nuevo estudiante
        estudiante = Estudiante(id_estudiante, nombre, active)

        # Guardar en archivo JSON
        data = self.file_manager.read()
        data.append(estudiante.to_dict())
        self.file_manager.save(data)
        print(f"Periodo registrado exitosamente con ID: {id_estudiante}.")

    def update(self):
        id_estudiante = input("Ingrese el ID del estudiante a actualizar: ")
        estudiantes = self.file_manager.find("id", int(id_estudiante))
        if estudiantes:
            estudiante = estudiantes[0]
            estudiante["nombre"] = input(f"Nombre actual ({estudiante['nombre']}): ") or estudiante["nombre"]
            active_input = input(f"Estado actual ({estudiante['estado']}): (S/N) ")
            if active_input:
                estudiante["estado"] = 'Activo' if active_input.lower() == 's' else 'Inactivo'

            data = self.file_manager.read()
            for i, e in enumerate(data):
                if e['id'] == int(id_estudiante):
                    data[i] = estudiante
                    break
            self.file_manager.save(data)
            print("Estudiante actualizado exitosamente.")
        else:
            print("Estudiante no encontrado.")

    def delete(self):
        id_estudiante = input("Ingrese el ID del estudiante a eliminar: ")
        data = self.file_manager.read()
        data = [e for e in data if e['id'] != int(id_estudiante)]
        self.file_manager.save(data)
        print("Estudiante eliminado exitosamente.")

    def consult(self):
        id_estudiante = input("Ingrese el ID del estudiante a consultar: ")
        estudiantes = self.file_manager.find("id", int(id_estudiante))
        if estudiantes:
            print(f"Estudiante encontrado: {estudiantes[0]}")
        else:
            print("Estudiante no encontrado.")
