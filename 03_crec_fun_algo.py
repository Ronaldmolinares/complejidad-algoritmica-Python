"""Para contar pasos, identifica cada operación: asignaciones y retornos valen 1.
Un bucle que no depende del input suma un valor constante (ej. 1000).
Los bucles dependientes de χ suman χ, y bucles anidados resultan en χ²."""


def f(x):
    respuesta = 0  # un paso (se realiza una asignación) --> 1
    for i in range(
        1000
    ):  # este loop ocurre 1000 veces (x (input) no influye en él)--> 1000
        respuesta += 1

    for i in range(x):  # loop que depende del valor de x --> X
        respuesta += x

    for i in range(x):  # --> X
        for j in range(x):  # --> X
            respuesta += 1  # asignación --> 1
            respuesta += 1  # asignación --> 1
            # 2χ²

    return respuesta  # operación --> 1


# Se obtiene una función polinomial: 2χ² + χ + 1002
