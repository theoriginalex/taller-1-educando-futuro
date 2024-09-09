from datetime import date
from clsJson import JsonFile
from iCrud import ICrud


class Profesor:
    def __init__(self, id, nombre, active=True, fecha_creacion=None):
        self.id = id
        self.nombre = nombre
        self.fecha_creacion = fecha_creacion if fecha_creacion else date.today()
        self.active = active

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'fecha_creacion': str(self.fecha_creacion),
            'active': 'Activo' if self.active else 'Inactivo'
        }

class CrudProfesores(ICrud):
    def __init__(self, json_file):
        self.file_manager = JsonFile(json_file)

    def _get_next_id(self):
        """ Obtiene el próximo ID basado en el último profesor registrado """
        data = self.file_manager.read()
        if data:
            last_id = data[-1]['id']  # Toma el último ID
            return last_id + 1  # Retorna el siguiente ID
        return 1  # Si no hay datos, comienza con 1

    def create(self):
        nombre = input("Ingrese el nombre del profesor: ")
        active = input("¿El profesor está activo? (S/N): ").lower() == 's'

        # Generar el nuevo ID automáticamente
        id_profesor = self._get_next_id()

        # Crear nuevo profesor
        profesor = Profesor(id_profesor, nombre, active)

        # Guardar en archivo JSON
        data = self.file_manager.read()
        data.append(profesor.to_dict())
        self.file_manager.save(data)
        print(f"Profesor registrado exitosamente con ID: {id_profesor}.")

    def update(self):
        id_profesor = input("Ingrese el ID del profesor a actualizar: ")
        profesores = self.file_manager.find("id", int(id_profesor))
        if profesores:
            profesor = profesores[0]
            profesor["nombre"] = input(f"Nombre actual ({profesor['nombre']}): ") or profesor["nombre"]
            active_input = input(f"Estado actual ({'Activo' if profesor['active'] == 'Activo' else 'Inactivo'}): (S/N) ")
            if active_input:
                profesor["active"] = 'Activo' if active_input.lower() == 's' else 'Inactivo'

            data = self.file_manager.read()
            for i, p in enumerate(data):
                if p['id'] == int(id_profesor):
                    data[i] = profesor
                    break
            self.file_manager.save(data)
            print("Profesor actualizado exitosamente.")
        else:
            print("Profesor no encontrado.")

    def delete(self):
        id_profesor = input("Ingrese el ID del profesor a eliminar: ")
        data = self.file_manager.read()
        data = [p for p in data if p['id'] != int(id_profesor)]
        self.file_manager.save(data)
        print("Profesor eliminado exitosamente.")

    def consult(self):
        id_profesor = input("Ingrese el ID del profesor a consultar: ")
        profesores = self.file_manager.find("id", int(id_profesor))
        if profesores:
            print(f"Profesor encontrado: {profesores[0]}")
        else:
            print("Profesor no encontrado.")
