from funcion_n import suma, resta, multiplicacion, division

def ejecutar():
    print("Prueba de Funciones")
    
    #suma
    resul_suma = suma(10, 5)
    print(f"Resultado de la suma (10 + 5): {resul_suma}")
    
    #resta
    resul_resta = resta(20, 8)
    print(f"Resultado de la resta (20 - 8): {resul_resta}")
    
    #multiplicacion
    resul_mult = multiplicacion(4, 5)
    print(f"Resultado de la multiplicación (4 * 5): {resul_mult}")

    #division
    resul_division = division(10, 2)
    print(f"Resultado de la division (10/2): {resul_division}")

if __name__ == "__main__":
    ejecutar_pruebas()