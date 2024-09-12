from datetime import date
from clsJson import JsonFile
from iCrud import ICrud


class Asignatura:
    def __init__(self, id, descripcion, nivel, active=True, fecha_creacion=None):
        self.id = id
        self.descripcion = descripcion
        self.nivel = nivel
        self.fecha_creacion = fecha_creacion if fecha_creacion else date.today()
        self.active = active

    def to_dict(self):
        return {
            'id': self.id,
            'descripcion': self.descripcion,
            'nivel': self.nivel,
            'fecha_creacion': str(self.fecha_creacion),
            'active': 'Activo' if self.active else 'Inactivo'
        }


class CrudAsignaturas(ICrud):
    def __init__(self, json_file):
        self.file_manager = JsonFile(json_file)

    def _get_next_id(self):
        """ Obtiene el próximo ID basado en la última asignatura registrada """
        data = self.file_manager.read()
        if data:
            last_id = data[-1]['id']  # Toma el último ID
            return last_id + 1  # Retorna el siguiente ID
        return 1  # Si no hay datos, comienza con 1

    def create(self):
        descripcion = input("Ingrese la descripción de la asignatura: ")
        nivel = input("Ingrese el nivel educativo de la asignatura: ")
        active = input("¿La asignatura está activa? (S/N): ").lower() == 's'

        # Generar el nuevo ID automáticamente
        id_asignatura = self._get_next_id()

        # Crear nueva asignatura
        asignatura = Asignatura(id_asignatura, descripcion, nivel, active)

        # Guardar en archivo JSON
        data = self.file_manager.read()
        data.append(asignatura.to_dict())
        self.file_manager.save(data)
        print(f"Asignatura registrada exitosamente con ID: {id_asignatura}.")

    def update(self):
        id_asignatura = input("Ingrese el ID de la asignatura a actualizar: ")
        asignaturas = self.file_manager.find("id", int(id_asignatura))
        if asignaturas:
            asignatura = asignaturas[0]
            asignatura["descripcion"] = input(f"Descripción actual ({asignatura['descripcion']}): ") or asignatura["descripcion"]
            asignatura["nivel"] = input(f"Nivel actual ({asignatura['nivel']}): ") or asignatura["nivel"]
            active_input = input(f"Estado actual ({'Activo' if asignatura['active'] == 'Activo' else 'Inactivo'}): (S/N) ")
            if active_input:
                asignatura["active"] = 'Activo' if active_input.lower() == 's' else 'Inactivo'

            data = self.file_manager.read()
            for i, a in enumerate(data):
                if a['id'] == int(id_asignatura):
                    data[i] = asignatura
                    break
            self.file_manager.save(data)
            print("Asignatura actualizada exitosamente.")
        else:
            print("Asignatura no encontrada.")

    def delete(self):
        id_asignatura = input("Ingrese el ID de la asignatura a eliminar: ")
        data = self.file_manager.read()
        data = [a for a in data if a['id'] != int(id_asignatura)]
        self.file_manager.save(data)
        print("Asignatura eliminada exitosamente.")

    def consult(self):
        id_asignatura = input("Ingrese el ID de la asignatura a consultar: ")
        asignaturas = self.file_manager.find("id", int(id_asignatura))
        if asignaturas:
            for i, j in asignaturas[0].items():
                print(f"{i}: {j}")
            #print(f"Asignatura encontrada: {asignaturas[0]}")
        else:
            print("Asignatura no encontrada.")
