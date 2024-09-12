from datetime import date
from clsJson import JsonFile
from iCrud import ICrud


class Nota:
    def __init__(self, id, periodo, profesor, asignatura, active=True, fecha_creacion=None):
        self.id = id
        self.periodo = periodo
        self.profesor = profesor
        self.asignatura = asignatura
        self.detalleNota = []
        self.fecha_creacion = fecha_creacion if fecha_creacion else date.today()
        self.estado = "Activo" if active else "Inactivo"

    def add_detalle(self, estudiante_id, calificacion):
        # Agrega un detalle de nota con el ID del estudiante y su calificación
        self.detalleNota.append({
            'estudiante_id': estudiante_id,
            'calificacion': calificacion
        })

    def to_dict(self):
        return {
            'id': self.id,
            'periodo': self.periodo,
            'profesor': self.profesor,
            'asignatura': self.asignatura,
            'detalleNota': self.detalleNota,
            'fecha_creacion': str(self.fecha_creacion),
            'estado': self.estado
        }


class CrudNotas(ICrud):
    def __init__(self, json_file):
        self.file_manager = JsonFile(json_file)

    def _get_next_id(self):
        """ Obtiene el próximo ID basado en el último registro de notas """
        data = self.file_manager.read()
        if data:
            last_id = data[-1]['id']  # Toma el último ID
            return last_id + 1  # Retorna el siguiente ID
        return 1  # Si no hay notas, comienza con 1

    def create(self):
        # Generar el nuevo ID automáticamente
        id_nota = self._get_next_id()

        periodo = input("Ingrese el periodo de la nota: ")
        profesor = input("Ingrese el nombre del profesor: ")
        asignatura = input("Ingrese la asignatura: ")
        activo = input("¿La nota está activa? (S/N): ").lower() == 's'
        nota = Nota(id_nota, periodo, profesor, asignatura, activo)

        # Agregar detalles de notas por estudiante
        while True:
            estudiante_id = input("Ingrese el ID del estudiante (o 'fin' para terminar): ")
            if estudiante_id.lower() == 'fin':
                break
            calificacion = float(input(f"Ingrese la calificación para el estudiante {estudiante_id}: "))
            nota.add_detalle(estudiante_id, calificacion)

        # Guardar en archivo JSON
        data = self.file_manager.read()
        data.append(nota.to_dict())
        self.file_manager.save(data)
        print(f"Nota registrada exitosamente con ID: {id_nota}.")

    def update(self):
        id_nota = input("Ingrese el ID de la nota a actualizar: ")
        notas = self.file_manager.find("id", int(id_nota))
        if notas:
            nota = notas[0]
            nota["periodo"] = input(f"Periodo actual ({nota['periodo']}): ") or nota["periodo"]
            nota["profesor"] = input(f"Profesor actual ({nota['profesor']}): ") or nota["profesor"]
            nota["asignatura"] = input(f"Asignatura actual ({nota['asignatura']}): ") or nota["asignatura"]
            estado_input = input(f"Estado actual ({nota['estado']}), ¿Cambiar? (S/N): ").lower()
            if estado_input == 's':
                nota["estado"] = "Activo" if input("¿La nota está activa? (S/N): ").lower() == 's' else "Inactivo"

            while True:
                editar_detalle = input("¿Desea editar un detalle de nota? (S/N): ").lower()
                if editar_detalle == 'n':
                    break
                estudiante_id = input("Ingrese el ID del estudiante a actualizar en el detalle: ")
                for detalle in nota["detalleNota"]:
                    if detalle["estudiante_id"] == estudiante_id:
                        detalle["calificacion"] = float(
                            input(f"Ingrese la nueva calificación para el estudiante {estudiante_id}: "))
                        break

            # Actualizar el archivo JSON
            data = self.file_manager.read()
            for i, nt in enumerate(data):
                if nt['id'] == int(id_nota):
                    data[i] = nota
                    break
            self.file_manager.save(data)
            print("Nota actualizada exitosamente.")
        else:
            print("Nota no encontrada.")

    def delete(self):
        id_nota = input("Ingrese el ID de la nota a eliminar: ")
        data = self.file_manager.read()
        data = [nt for nt in data if nt['id'] != int(id_nota)]
        self.file_manager.save(data)
        print("Nota eliminada exitosamente.")

    def consult(self):
        id_nota = input("Ingrese el ID de la nota a consultar: ")
        notas = self.file_manager.find("id", int(id_nota))
        if notas:
            for i, j in notas[0].items():
                print(f"{i}: {j}")
            print(f"Nota encontrada: {notas[0]}")
        else:
            print("Nota no encontrada.")


