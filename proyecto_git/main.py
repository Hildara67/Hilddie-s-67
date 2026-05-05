import matplotlib.pyplot as plt

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


    plt.figure() 
    plt.bar(['Suma', 'Resta'], [resul_suma, resul_resta], color='blue')
    plt.title("Resultados: Suma y Resta")
    plt.savefig("grafica_operaciones_1.eps") 
    print("Archivo .eps generado (Suma y Resta).")

    plt.figure() 
    plt.bar(['Multiplicación', 'División'], [resul_mult, resul_division], color='green')
    plt.title("Resultados: Multiplicación y División")
    plt.savefig("grafica_operaciones_2.eps")
    print("Archivo .eps generado (Multiplicación y División).")

if __name__ == "__main__":
    ejecutar()