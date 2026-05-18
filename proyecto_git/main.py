from funcion_n import fibonacci, factorial, es_primo

def main():
    print("=== Bienvenido al proyecto Git ===")
    num = 10
    print(f"Fibonacci de {num}: {fibonacci(num)}")
    print(f"Factorial de {num}: {factorial(num)}")
    print(f"¿{num} es primo?: {es_primo(num)}")

if __name__ == "__main__":
    main()
