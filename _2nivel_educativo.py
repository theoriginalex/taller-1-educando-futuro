from datetime import date
from clsJson import JsonFile
from iCrud import ICrud


class NivelesEducativos:
    def __init__(self, id, nombre_nivel, active=True, fecha_creacion=None):
        self.id = id
        self.nombre_nivel = nombre_nivel
        self.fecha_creacion = fecha_creacion if fecha_creacion else date.today()
        self.active = active

    def to_dict(self):
        return {
            'id': self.id,
            'nombre_nivel': self.nombre_nivel,
            'fecha_creacion': str(self.fecha_creacion),
            'active': 'Activo' if self.active else 'Inactivo'
        }


class CrudNivelesEducativos(ICrud):
    def __init__(self, json_file):
        self.file_manager = JsonFile(json_file)

    def _get_next_id(self):
        """ Obtiene el próximo ID basado en el último nivel registrado """
        data = self.file_manager.read()
        if data:
            last_id = data[-1]['id']  # Toma el último ID
            return last_id + 1  # Retorna el siguiente ID
        return 1  # Si no hay datos, comienza con 1

    def create(self):
        nombre_nivel = input("Ingrese el nombre del nivel educativo: ")
        active = input("¿El nivel está activo? (S/N): ").lower() == 's'

        # Generar el nuevo ID automáticamente
        id_nivel = self._get_next_id()

        # Crear nuevo nivel educativo
        nivel = NivelesEducativos(id_nivel, nombre_nivel, active)

        # Guardar en archivo JSON
        data = self.file_manager.read()
        data.append(nivel.to_dict())
        self.file_manager.save(data)
        print(f"Nivel educativo registrado exitosamente con ID: {id_nivel}.")

    def update(self):
        id_nivel = input("Ingrese el ID del nivel educativo a actualizar: ")
        niveles = self.file_manager.find("id", int(id_nivel))
        if niveles:
            nivel = niveles[0]
            nivel["nombre_nivel"] = input(f"Nombre actual ({nivel['nombre_nivel']}): ") or nivel["nombre_nivel"]
            active_input = input(f"Estado actual ({'Activo' if nivel['active'] == 'Activo' else 'Inactivo'}): (S/N) ")
            if active_input:
                nivel["active"] = 'Activo' if active_input.lower() == 's' else 'Inactivo'

            data = self.file_manager.read()
            for i, n in enumerate(data):
                if n['id'] == int(id_nivel):
                    data[i] = nivel
                    break
            self.file_manager.save(data)
            print("Nivel educativo actualizado exitosamente.")
        else:
            print("Nivel educativo no encontrado.")

    def delete(self):
        id_nivel = input("Ingrese el ID del nivel educativo a eliminar: ")
        data = self.file_manager.read()
        data = [n for n in data if n['id'] != int(id_nivel)]
        self.file_manager.save(data)
        print("Nivel educativo eliminado exitosamente.")

    def consult(self):
        id_nivel = input("Ingrese el ID del nivel educativo a consultar: ")
        niveles = self.file_manager.find("id", int(id_nivel))
        if niveles:
            for i, j in niveles[0].items():
                print(f"{i}: {j}")
            #print(f"Nivel educativo encontrado: {niveles[0]}")
        else:
            print("Nivel educativo no encontrado.")
