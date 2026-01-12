from bokeh.plotting import figure, output_file, show

if __name__ == "__main__":
    output_file("Graficado_simple.html")  # definimos el archivo de salida
    fig = figure()  # objeto para dibujar los datos
    type(fig)

    total_value = int(input("Cuantos valores quieres graficar?: "))
    x_vals = list(range(total_value))
    y_vals = []

    for x in x_vals:
        val = int(input(f"Valor de x para y {x}: "))
        y_vals.append(val)

    fig.line(x_vals, y_vals, line_width=2)
    show(fig)
