from Unidades import obtener_poder_unidades
from Recursos import obtener_recursos_disponibles

def definir_variables():
    """Define las variables para el problema de optimización."""
    return {'swordsmen': 0, 'bowmen': 0, 'horsemen': 0}

def verificar_restricciones(variables, recursos_disponibles):
    """Verifica si las restricciones se cumplen."""
    swordsmen, bowmen, horsemen = variables['swordsmen'], variables['bowmen'], variables['horsemen']
    comida = swordsmen * 60 + bowmen * 80 + horsemen * 140
    madera = swordsmen * 20 + bowmen * 10
    oro = bowmen * 40 + horsemen * 100

    return (comida <= recursos_disponibles['comida'] and
            madera <= recursos_disponibles['madera'] and
            oro <= recursos_disponibles['oro'])

def calcular_poder(variables, poder_unidades):
    """Calcula el poder total del ejército."""
    swordsmen, bowmen, horsemen = variables['swordsmen'], variables['bowmen'], variables['horsemen']
    return (swordsmen * poder_unidades['swordsmen'] +
            bowmen * poder_unidades['bowmen'] +
            horsemen * poder_unidades['horsemen'])

def optimizar_ejercito():
    """Optimiza la composición del ejército para maximizar el poder."""
    poder_unidades = obtener_poder_unidades()
    recursos_disponibles = obtener_recursos_disponibles()

    mejor_poder = 0
    mejor_combinacion = None

    # Búsqueda exhaustiva (puedes optimizar esto con otro enfoque si es necesario)
    for swordsmen in range(0, recursos_disponibles['comida'] // 60 + 1):
        for bowmen in range(0, recursos_disponibles['comida'] // 80 + 1):
            for horsemen in range(0, recursos_disponibles['comida'] // 140 + 1):
                variables = {'swordsmen': swordsmen, 'bowmen': bowmen, 'horsemen': horsemen}
                if verificar_restricciones(variables, recursos_disponibles):
                    poder_actual = calcular_poder(variables, poder_unidades)
                    if poder_actual > mejor_poder:
                        mejor_poder = poder_actual
                        mejor_combinacion = variables

    return mejor_combinacion, mejor_poder

def main():
    mejor_combinacion, mejor_poder = optimizar_ejercito()

    if mejor_combinacion:
        print('Solución óptima encontrada:')
        print(f'Swordsmen: {mejor_combinacion["swordsmen"]}')
        print(f'Bowmen: {mejor_combinacion["bowmen"]}')
        print(f'Horsemen: {mejor_combinacion["horsemen"]}')
        print(f'Poder máximo: {mejor_poder}')
    else:
        print('No se encontró una solución óptima.')

if __name__ == '__main__':
    main()