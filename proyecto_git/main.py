import matplotlib.pyplot as plt

from funcion_n import suma, resta, multiplicacion, division, fibonacci, factorial, es_primo

def ejecutar():
    print("Prueba de Funciones")

    resul_suma = suma(10, 5)
    print(f"Resultado de la suma (10 + 5): {resul_suma}")

    resul_resta = resta(20, 8)
    print(f"Resultado de la resta (20 - 8): {resul_resta}")

    resul_mult = multiplicacion(4, 5)
    print(f"Resultado de la multiplicacion (4 * 5): {resul_mult}")

    resul_division = division(10, 2)
    print(f"Resultado de la division (10/2): {resul_division}")

    plt.figure()
    plt.bar(['Suma', 'Resta'], [resul_suma, resul_resta], color='blue')
    plt.title("Resultados: Suma y Resta")
    plt.savefig("grafica_operaciones_1.eps")
    print("Archivo .eps generado (Suma y Resta).")

    plt.figure()
    plt.bar(['Multiplicacion', 'Division'], [resul_mult, resul_division], color='green')
    plt.title("Resultados: Multiplicacion y Division")
    plt.savefig("grafica_operaciones_2.eps")
    print("Archivo .eps generado (Multiplicacion y Division).")

    num = 10
    print(f"Fibonacci de {num}: {fibonacci(num)}")
    print(f"Factorial de {num}: {factorial(num)}")
    print(f"¿{num} es primo?: {es_primo(num)}")

if __name__ == "__main__":
    ejecutar()
