from clsJson import JsonFile
from iCrud import ICrud


class DetalleNota:
    def __init__(self, id, estudiante, nota1, nota2, recuperacion=None, observacion=None):
        self.id = id
        self.estudiante = estudiante
        self.nota1 = nota1
        self.nota2 = nota2
        self.recuperacion = recuperacion
        self.observacion = observacion

    def to_dict(self):
        return {
            'id': self.id,
            'estudiante': self.estudiante,
            'nota1': self.nota1,
            'nota2': self.nota2,
            'recuperacion': self.recuperacion,
            'observacion': self.observacion
        }


class CrudDetalleNotas(ICrud):
    def __init__(self, json_file):
        self.file_manager = JsonFile(json_file)

    def _get_next_id(self):
        """Obtiene el próximo ID basado en el último registro de detalles de notas"""
        data = self.file_manager.read()
        if data:
            last_id = data[-1]['id']  # Toma el último ID
            return last_id + 1  # Retorna el siguiente ID
        return 1  # Si no hay registros, comienza con 1

    def create(self):
        # Generar el nuevo ID automáticamente
        id_detalle = self._get_next_id()

        estudiante = input("Ingrese el nombre del estudiante: ")
        nota1 = float(input("Ingrese la primera calificación: "))
        nota2 = float(input("Ingrese la segunda calificación: "))
        recuperacion = input("Ingrese la nota de recuperación (opcional, presione enter si no aplica): ")
        recuperacion = float(recuperacion) if recuperacion else None
        observacion = input("Ingrese alguna observación (opcional): ")

        detalle_nota = DetalleNota(id_detalle, estudiante, nota1, nota2, recuperacion, observacion)

        # Guardar en archivo JSON
        data = self.file_manager.read()
        data.append(detalle_nota.to_dict())
        self.file_manager.save(data)
        print(f"Detalle de nota registrado exitosamente con ID: {id_detalle}.")

    def update(self):
        id_detalle = input("Ingrese el ID del detalle de nota a actualizar: ")
        detalles = self.file_manager.find("id", int(id_detalle))
        if detalles:
            detalle = detalles[0]
            detalle["estudiante"] = input(f"Estudiante actual ({detalle['estudiante']}): ") or detalle["estudiante"]
            detalle["nota1"] = float(input(f"Primera calificación actual ({detalle['nota1']}): ") or detalle["nota1"])
            detalle["nota2"] = float(input(f"Segunda calificación actual ({detalle['nota2']}): ") or detalle["nota2"])
            recuperacion_input = input(f"Recuperación actual ({detalle['recuperacion']}): (opcional) ")
            if recuperacion_input:
                detalle["recuperacion"] = float(recuperacion_input)
            observacion_input = input(f"Observación actual ({detalle['observacion']}): (opcional) ")
            if observacion_input:
                detalle["observacion"] = observacion_input

            # Actualizar en archivo JSON
            data = self.file_manager.read()
            for i, dt in enumerate(data):
                if dt['id'] == int(id_detalle):
                    data[i] = detalle
                    break
            self.file_manager.save(data)
            print("Detalle de nota actualizado exitosamente.")
        else:
            print("Detalle de nota no encontrado.")

    def delete(self):
        id_detalle = input("Ingrese el ID del detalle de nota a eliminar: ")
        data = self.file_manager.read()
        data = [dt for dt in data if dt['id'] != int(id_detalle)]
        self.file_manager.save(data)
        print("Detalle de nota eliminado exitosamente.")

    def consult(self):
        id_detalle = input("Ingrese el ID del detalle de nota a consultar: ")
        detalles = self.file_manager.find("id", int(id_detalle))
        if detalles:
            for i, j in detalles[0].items():
                print(f"{i}: {j}")
            #print(f"Detalle de nota encontrado: {detalles[0]}")
        else:
            print("Detalle de nota no encontrado.")

