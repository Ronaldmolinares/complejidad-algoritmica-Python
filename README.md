# Complejidad Algorítmica en Python

Repositorio para recordar conceptos fundamentales de **análisis de algoritmos**, **complejidad computacional** y **algoritmos de optimización** implementados en Python.

## Contenido

### 🔍 Análisis de Complejidad Algorítmica

Este repositorio incluye implementaciones prácticas de las principales clases de complejidad: 

- **O(1)** - Constante
- **O(log n)** - Logarítmica
- **O(n)** - Lineal
- **O(n log n)** - Log lineal
- **O(n²)** - Polinomial
- **O(2ⁿ)** - Exponencial

### 📊 Algoritmos de Búsqueda

#### Búsqueda Lineal (`06_busqueda_lineal.py`)
- **Complejidad**:  O(n)
- Búsqueda secuencial elemento por elemento
- Útil para listas no ordenadas

#### Búsqueda Binaria (`07_busqueda_binaria.py`)
- **Complejidad**:  O(log n)
- Requiere lista ordenada
- Divide el espacio de búsqueda a la mitad en cada iteración

### 🔄 Algoritmos de Ordenamiento

#### 1. Ordenamiento Burbuja (`08_burbuja.py`)
```python
def burbuja(lista):  # Complejidad O(n²)
    n = len(lista)
    for pasada in range(n):
        for j in range(0, n - pasada - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
```

**Características:**
- **Complejidad temporal**: O(n²) en todos los casos
- **Complejidad espacial**: O(1)
- Simple pero ineficiente para listas grandes
- Compara elementos adyacentes repetidamente

#### 2. Ordenamiento por Inserción (`09_insertion_sort.py`)
```python
def insertion_sort(lista):
    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion = indice
        while posicion > 0 and lista[posicion - 1] > valor_actual:
            lista[posicion] = lista[posicion - 1]
            posicion -= 1
        lista[posicion] = valor_actual
    return lista
```

**Características:**
- **Mejor caso**: O(n) - lista ya ordenada
- **Peor caso**: O(n²) - lista en orden inverso
- **Complejidad espacial**: O(1)
- Eficiente para listas pequeñas o casi ordenadas
- Algoritmo estable

#### 3. Merge Sort (`10_merge_sort.py`)
```python
def merge_sort(lista):
    if len(lista) > 1:
        mitad = len(lista) // 2
        izquierda = lista[:mitad]
        derecha = lista[mitad:]
        
        merge_sort(izquierda)
        merge_sort(derecha)
        
        # Mezclar las sublistas ordenadas
        ... 
    return lista
```

**Características:**
- **Complejidad temporal**: O(n log n) en todos los casos
- **Complejidad espacial**: O(n)
- Algoritmo de divide y conquista
- Mantiene el orden relativo (estable)
- Ideal para listas grandes

**Ventajas:**
- Rendimiento predecible O(n log n)
- Estable y eficiente
- Funciona bien con datos grandes

**Desventajas:**
- Requiere espacio adicional O(n)
- No es "in-place" como otros algoritmos

### 🎒 Problema de la Mochila (Knapsack Problem)

Implementación del clásico **0-1 Knapsack Problem** usando programación recursiva. 

#### Descripción del Problema
Dado un conjunto de elementos, cada uno con un peso y un valor, determinar qué elementos incluir en una mochila de capacidad limitada para maximizar el valor total, sin poder dividir los elementos. 

#### Implementación (`problema_morral.py`)

```python
def morral(tamano_morral, pesos, valores, n):
    # Caso base 1: Sin elementos o sin espacio
    if n == 0 or tamano_morral == 0:
        return 0
    
    # Caso base 2: Elemento no cabe
    if pesos[n - 1] > tamano_morral:
        return morral(tamano_morral, pesos, valores, n - 1)
    
    # Decisión: tomar o no el elemento
    return max(
        valores[n - 1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n - 1),
        morral(tamano_morral, pesos, valores, n - 1)
    )
```

**Características:**
- **Complejidad**: O(2ⁿ) - Exponencial
- Solución recursiva que explora todas las combinaciones
- Incluye versión verbose para visualizar el proceso de decisión
- Cada elemento se considera dos veces (tomarlo o dejarlo)

**Casos Base:**
1. No quedan elementos o no hay capacidad → retorna 0
2. El elemento pesa más que la capacidad disponible → lo descarta

**Optimizaciones posibles:**
- Programación dinámica (memoización)
- Enfoque iterativo bottom-up
- Reducción de complejidad a O(n × W) donde W es la capacidad

### 📈 Comparación de Eficiencia

El archivo `02_compar_eficien. py` compara implementaciones recursivas vs iterativas:

- **Factorial recursivo vs tradicional**
- **Fibonacci recursivo vs tradicional**

Demostrando que: 
- Las soluciones iterativas suelen ser más eficientes
- La recursión puede ser más elegante pero costosa en memoria
- Python tiene límites de recursión que pueden ajustarse

### 📊 Clases de Complejidad (`05_clases_comp_alg.py`)

Análisis práctico con medición de tiempo de ejecución para diferentes complejidades:

| Complejidad | n=10 | n=100 | n=1000 |
|-------------|------|-------|--------|
| O(1) | Constante | Constante | Constante |
| O(log n) | ~1 | ~2 | ~3 |
| O(n) | 10 | 100 | 1000 |
| O(n log n) | ~10 | ~200 | ~3000 |
| O(n²) | 100 | 10000 | 1000000 |
| O(2ⁿ) | 1024 | 2¹⁰⁰ | Inviable |

## 🚀 Uso

### Requisitos
- Python 3.x
- Dependencias básicas (incluidas en stdlib)

### Ejecutar ejemplos

```bash
# Algoritmos de ordenamiento
python 08_burbuja.py
python 09_insertion_sort. py
python 10_merge_sort.py

# Problema de la mochila
python problema_morral.py

# Análisis de complejidad
python 05_clases_comp_alg.py

# Comparación de eficiencia
python 02_compar_eficien.py
```

## 📚 Conceptos Clave

### Notación Big O
La notación Big O describe el comportamiento asintótico de un algoritmo: 
- **Mejor caso**:  Escenario más favorable
- **Caso promedio**: Comportamiento típico esperado
- **Peor caso**: Escenario menos favorable

### Análisis de Algoritmos
1. **Complejidad Temporal**:  Tiempo de ejecución en función del tamaño de entrada
2. **Complejidad Espacial**: Memoria requerida
3. **Trade-offs**: Balance entre tiempo y espacio

### Estrategias de Diseño
- **Fuerza bruta**: Explorar todas las posibilidades
- **Divide y conquista**:  Dividir el problema en subproblemas
- **Programación dinámica**: Reutilizar soluciones a subproblemas
- **Algoritmos voraces (greedy)**: Tomar decisiones localmente óptimas

## 🎯 Casos de Uso

### Cuándo usar cada algoritmo

**Ordenamiento Burbuja:**
- Listas muy pequeñas (< 10 elementos)
- Propósitos educativos
- Cuando la simplicidad es prioritaria

**Insertion Sort:**
- Listas pequeñas o casi ordenadas
- Datos que llegan en tiempo real
- Cuando se necesita estabilidad y simplicidad

**Merge Sort:**
- Listas grandes
- Cuando se necesita rendimiento predecible
- Datos en memoria externa
- Cuando la estabilidad es importante

**Problema de la Mochila:**
- Optimización de recursos limitados
- Problemas de selección con restricciones
- Planificación y asignación de recursos

## 📖 Recursos Adicionales

- [Big O Cheat Sheet](https://www.bigocheatsheet.com/)
- [Visualización de Algoritmos](https://visualgo.net/)
- [Python Time Complexity](https://wiki.python.org/moin/TimeComplexity)

---

**Autor**: @Ronaldmolinares  
**Enfoque**: Análisis de Algoritmos y Estructuras de Datos en Python
