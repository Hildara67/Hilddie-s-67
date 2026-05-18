import numpy as np

def calcular_estadisticas(datos):
    media = np.mean(datos)
    mediana = np.median(datos)
    desviacion = np.std(datos)
    return media, mediana, desviacion

def main():
    datos = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    media, mediana, desviacion = calcular_estadisticas(datos)
    print(f"Datos: {datos}")
    print(f"Media: {media:.2f}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Desviacion estandar: {desviacion:.2f}")
    print(f"Suma: {np.sum(datos)}")
    print(f"Producto: {np.prod(datos)}")

if __name__ == "__main__":
    main()
