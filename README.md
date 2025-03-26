# Algoritmos y Estructuras de Datos

## Lab02: Recursion and Backtracking

### Capacidades

- Conocer, comprender y aplicar los algoritmos de recursión y backtracking en la resolución de problemas de software.

### Seguridad

- Generar un ambiente seguro.
- Evitar el consumo de alimentos.
- Dejar el ambiente ordenado y limpio.

### Preparación

El alumno debe revisar previamente el material cargado.

### Recursos

- Computadora.

### Instrucciones

Cada integrante del grupo debe seleccionar un ejercicio diferente y desarrollarlo con la siguiente estructura:

1. Nombre del alumno
2. Ejercicio a desarrollar
3. Prompt engineering
4. Prompt ingresado y captura
5. Análisis del prompt
6. Ajustes del prompt y captura
7. Comentarios de los compañeros
8. Código
9. Código desarrollado
10. Análisis del código
11. Captura de la ejecución del código
12. Comentarios de los compañeros

> **Nota:** Desarrollar todo el código en inglés.

### Bibliotecas

- [https://matplotlib.org/stable/users/installing/index.html](https://matplotlib.org/stable/users/installing/index.html)

## Ejercicios

### Recursividad

#### 1. Factorial

- Explicar cómo funciona el algoritmo.
- Graficar el tiempo que demora en ejecutar una función factorial para los valores: 1,2,4,8,16,32,64,128,256,512,1024, 2048, 2080, 2100, 4096.
- Hacer su diagrama de flujo.
- Comentarios del problema.
- ¿Es posible aumentar el tamaño del stack?

#### 2. Torre de Hanoi

- Explicar cómo funciona el algoritmo.
- Graficar el tiempo que demora en resolverse una torre de Hanoi de: 1,2,3,4,5,6,7,8,9,10,11,12,13,14 discos.
- Hacer su diagrama de flujo.
- Comentarios del problema.
- ¿Es posible aumentar el tamaño del stack?

### Backtracking

#### 1. Binary

- Explicar cómo funciona el algoritmo.
- Calcule el valor de permutación para 3,4,5,6 bits.
- Hacer su diagrama de flujo.
- Comentarios del problema.
- ¿Es posible aumentar el tamaño del stack?

#### 2. Proponer un algoritmo que emplee backtracking y resuelva un problema

- Explicar cómo funciona el algoritmo.
- Explorar todas las direcciones posibles.
- Retroceder si se encuentra un camino bloqueado.
- Terminar cuando se encuentre la salida o si no hay solución.
- Hacer su diagrama de flujo.
- Comentarios del problema.

## Soluciones

### Factorial (Josue Zapata Villegas)

- Descripción del problema: La función factorial calcula el producto de todos los enteros positivos desde 1 hasta un número dado `n!`. Ejemplo: \( n! = n \times (n-1) \times (n-2) \times ... \times 1 \)

- **Código Implementado:**

```python
import time

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    print(factorial(9))
```

- **Comentarios del problema:**

  El cálculo factorial mediante recursión puede causar un "RecursionError" debido al límite de recursión de Python (aproximadamente 1000 llamadas recursivas por defecto).

### Torre de Hanoi (Yamile Ochoa Marin)

- Descripción del problema: Mover un conjunto de discos de una torre a otra utilizando una torre auxiliar, siguiendo las reglas:

    1. Solo se puede mover un disco a la vez.
    2. Un disco más grande no puede estar sobre uno más pequeño.
    3. Solo se puede mover el disco superior de una torre.

- **Código Implementado:**

```python
def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n - 1, auxiliary, target, source)

if __name__ == "__main__":
    hanoi(3, 'A', 'C', 'B')
```

- **Comentarios del problema:**

    - El algoritmo tiene complejidad \(O(2^n)\) debido a la cantidad exponencial de movimientos necesarios.

### Binary (Salva Saccatoma Rodrigo)

- Descripción del problema: Generar todas las cadenas binarias de longitud `n` utilizando recursión y backtracking.

- **Código Implementado:**

```python
def generate_binary(n, result=""):
    if len(result) == n:
        print(result)
        return
    generate_binary(n, result + "0")
    generate_binary(n, result + "1")

if __name__ == "__main__":
    generate_binary(3)
```

- **Comentarios del problema:**

    - Este enfoque genera todas las posibles combinaciones binarias con una complejidad \(O(2^n)\).

### Propuesta de Algoritmo (Araujo Gabriel Yair Smith)

- Descripción del problema: Encontrar todas las formas de sumar un número `N` usando solo {1, 2, 3}.

- **Código Implementado:**

```python
def find_combinations(N, current=[]):
    if sum(current) == N:
        print(current)
        return
    if sum(current) > N:
        return

    for i in [1, 2, 3]:
        find_combinations(N, current + [i])

if __name__ == "__main__":
    find_combinations(4)
```

- **Comentarios del problema:**

    - Este algoritmo usa backtracking para encontrar todas las combinaciones posibles.

## Conclusiones

- La recursión permite resolver problemas dividiéndolos en subproblemas más pequeños.
- Los algoritmos recursivos pueden causar problemas de rendimiento debido al uso intensivo de la pila de llamadas.
- El backtracking es útil para explorar todas las posibles soluciones en problemas de búsqueda complejos.
