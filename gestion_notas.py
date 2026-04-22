"""
Módulo de gestión de notas de estudiantes.

Permite registrar estudiantes con sus calificaciones,
calcular promedios y generar informes académicos.
"""

# Constantes de configuración del sistema
NOTA_MINIMA = 0
NOTA_MAXIMA = 10
NOTA_APROBADO = 5


class GestorNotas:
    """Gestiona las calificaciones de un grupo de estudiantes.

    Attributes:
        estudiantes (list[dict]): Lista de registros de estudiantes.
    """

    def __init__(self):
        """Inicializa el gestor con una lista vacía de estudiantes."""
        self.estudiantes = []

    # --- Métodos de validación ---

    def _validar_notas(self, notas):
        """Comprueba que todas las notas estén en el rango permitido.

        Args:
            notas (list[float]): Lista de calificaciones a validar.

        Returns:
            bool: True si todas las notas son válidas, False en caso contrario.
        """
        return all(NOTA_MINIMA <= nota <= NOTA_MAXIMA for nota in notas)

    # --- Métodos de cálculo ---

    def _calcular_promedio(self, notas):
        """Calcula el promedio de una lista de notas.

        Args:
            notas (list[float]): Lista de calificaciones.

        Returns:
            float: Promedio de las notas, o 0.0 si la lista está vacía.
        """
        if not notas:
            return 0.0
        return sum(notas) / len(notas)

    def _determinar_resultado(self, promedio):
        """Determina si el estudiante aprueba o suspende.

        Args:
            promedio (float): Nota media del estudiante.

        Returns:
            str: "aprobado" si promedio >= NOTA_APROBADO, "suspenso" en caso contrario.
        """
        return "aprobado" if promedio >= NOTA_APROBADO else "suspenso"

    # --- Métodos principales ---

    def registrar_estudiante(self, nombre, notas):
        """Registra un estudiante con sus calificaciones.

        Args:
            nombre (str): Nombre completo del estudiante.
            notas (list[float]): Lista de calificaciones.

        Returns:
            dict | None: Registro del estudiante o None si las notas son inválidas.
        """
        if not self._validar_notas(notas):
            print(f"Error: las notas de {nombre} no son válidas.")
            return None

        promedio = self._calcular_promedio(notas)
        resultado = self._determinar_resultado(promedio)

        registro = {
            "nombre": nombre,
            "notas": notas,
            "promedio": round(promedio, 2),
            "resultado": resultado,
        }
        self.estudiantes.append(registro)
        return registro

    def buscar_estudiante(self, nombre):
        """Busca un estudiante por nombre.

        Args:
            nombre (str): Nombre a buscar.

        Returns:
            dict | None: Registro del estudiante o None si no se encuentra.
        """
        for estudiante in self.estudiantes:
            if estudiante["nombre"] == nombre:
                return estudiante
        return None

    def mostrar_informe(self):
        """Muestra un informe con las calificaciones de todos los estudiantes."""
        if not self.estudiantes:
            print("No hay estudiantes registrados.")
            return

        # Detalle individual
        for est in self.estudiantes:
            print(
                f"Nombre: {est['nombre']} | "
                f"Promedio: {est['promedio']} | "
                f"{est['resultado'].capitalize()}"
            )

        print("---")

        # Estadísticas generales
        total_promedios = sum(e["promedio"] for e in self.estudiantes)
        media_general = total_promedios / len(self.estudiantes)
        aprobados = sum(1 for e in self.estudiantes if e["resultado"] == "aprobado")
        suspensos = len(self.estudiantes) - aprobados

        print(f"Media general: {media_general:.2f}")
        print(f"Aprobados: {aprobados} | Suspensos: {suspensos}")


# --- Ejecución principal ---
if __name__ == "__main__":
    gestor = GestorNotas()

    gestor.registrar_estudiante("Ana", [7, 8, 6, 9])
    gestor.registrar_estudiante("Luis", [4, 3, 5, 2])
    gestor.registrar_estudiante("Marta", [10, 9, 8, 10])
    gestor.registrar_estudiante("Pedro", [3, 2, 1, 4])

    gestor.mostrar_informe()

    resultado = gestor.buscar_estudiante("Marta")
    if resultado is not None:
        print(f"Encontrado: {resultado['nombre']}")
