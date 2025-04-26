import pulp

class Poder:
    def __init__(self, recursos, unidades):
        self.recursos = recursos
        self.unidades = unidades

    def maximizar_poder(self):
        # Crear el problema
        model = pulp.LpProblem("Maximizar_Poder_Ejercito", pulp.LpMaximize)

        # Variables de decisión para cada unidad
        variables = {unidad.nombre: pulp.LpVariable(unidad.nombre, lowBound=0, cat='Integer') for unidad in self.unidades}

        # Función objetivo: maximizar el poder total
        model += pulp.lpSum(variables[unidad.nombre] * unidad.poder for unidad in self.unidades)

        # Restricciones de recursos
        model += pulp.lpSum(variables[unidad.nombre] * unidad.comida for unidad in self.unidades) <= self.recursos.comida.cantidad, "Restriccion_Comida"
        model += pulp.lpSum(variables[unidad.nombre] * unidad.madera for unidad in self.unidades) <= self.recursos.madera.cantidad, "Restriccion_Madera"
        model += pulp.lpSum(variables[unidad.nombre] * unidad.oro for unidad in self.unidades) <= self.recursos.oro.cantidad, "Restriccion_Oro"

        # Resolver
        model.solve()

        # Resultado
        resultado = {unidad.nombre: int(variables[unidad.nombre].varValue) for unidad in self.unidades}
        poder_total = pulp.value(model.objective)
        
        return resultado, poder_total
