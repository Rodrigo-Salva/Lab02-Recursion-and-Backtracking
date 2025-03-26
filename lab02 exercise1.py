import sys
import time
import matplotlib.pyplot as plt

sys.setrecursionlimit(5000)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n_values = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 2080, 2100, 4096]
execution_times = []

for n in n_values:
    start_time = time.time()
    factorial(n)  
    end_time = time.time()
    execution_times.append(end_time - start_time)

# Graficar los resultados
plt.figure(figsize=(10, 5))
plt.plot(n_values, execution_times, marker='o', linestyle='-')
plt.xlabel("n (valor del factorial)")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.title("Tiempo de ejecución de la función factorial recursiva")
plt.grid()
plt.show()
