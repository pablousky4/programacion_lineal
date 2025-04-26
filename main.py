from Recursos.recursos import Recursos
from Unidades.espadachines import Espadachin
from Unidades.arqueros import Arquero
from Unidades.jinetes import Jinete
from Poder import Poder

def main():
    # Inicializar recursos
    recursos = Recursos(comida=1200, madera=800, oro=600)

    # Inicializar unidades
    unidades = [Espadachin(), Arquero(), Jinete()]

    # Crear el modelo de poder
    modelo_poder = Poder(recursos, unidades)

    # Maximizar el poder
    resultado, poder_total = modelo_poder.maximizar_poder()

    # Mostrar resultados
    print("Plan Óptimo de Entrenamiento de Unidades:")
    for unidad, cantidad in resultado.items():
        print(f"  - {unidad}: {cantidad}")
    print(f"\nPoder Total Máximo: {poder_total}")

if __name__ == "__main__":
    main()
