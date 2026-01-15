from tkinter import Tk, Label, Entry, Button
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def ejemplo_reales():
    # a = 1 b = 4 c = 0
    # a = 1 b = 2 c = 6
    limpiar()
    a.insert(0, "1")
    b.insert(0, "4")
    c.insert(0, "0")


def ejemplo_complejos():
    limpiar()
    a.insert(0, "1")
    b.insert(0, "2")
    c.insert(0, "6")


def limpiar():
    fallo.config(text="")
    a.delete(0, "end")
    b.delete(0, "end")
    c.delete(0, "end")


def resolver_ecuacion():
    try:
        var_a = float(a.get())
        var_b = float(b.get())
        var_c = float(c.get())
        if var_b**2 >= 4 * var_a * var_c:
            rx1 = (-var_b + sqrt((var_b**2) - (4 * var_a * var_c))) / (2 * var_a)
            rx2 = (-var_b - sqrt((var_b**2) - (4 * var_a * var_c))) / (2 * var_a)
            x1.config(text=f"x1 = {rx1:.3f}")
            x2.config(text=f"x2 = {rx2:.3f}")
            fallo.config(text="")
        else:
            fallo.config(text="Solucion compleja")
    except ValueError:
        fallo.config(text="Error: Debes poner números")


def graficar():
    # 1. Crear la figura de Matplotlib
    fig, ax = plt.subplots(figsize=(5, 4), dpi=100)

    # 2. Obtener los valores de los Entry (asumiendo que se llaman a, b, c)
    try:
        val_a = float(a.get())
        val_b = float(b.get())
        val_c = float(c.get())
    except:
        # Valores por defecto si hay error
        val_a, val_b, val_c = 1, 2, 5

    x = np.linspace(-10, 10, 400)
    y = val_a * x**2 + val_b * x + val_c

    ax.plot(x, y)
    ax.axhline(0, color="black", linewidth=1)
    ax.axvline(0, color="black", linewidth=1)
    ax.set_title("Gráfica de la Función Cuadrática")
    ax.grid(True)

    # 3. Crear el widget de Tkinter que contiene la gráfica
    canvas = FigureCanvasTkAgg(fig, master=ventana)  # 'ventana' es tu Tk()
    canvas_widget = canvas.get_tk_widget()

    # 4. Ubicar el widget en la ventana (puedes usar pack, grid o place)
    canvas_widget.place(x=700, y=100)  # Ajusta las coordenadas a tu gusto
    canvas.draw()


ventana = Tk()
ventana.attributes("-topmost", True)
ventana.geometry("1280x900")
ventana.title("sistema para resolver funciones de segundo grado")
titulo = Label(
    ventana,
    text="sistema para encontrar las raices de una ecuacion cuadratica",
    font=("Arial", 24),
)
titulo.place(x=0, y=0)
constantes = Label(ventana, text="a =  \n\n b =  \n\n c = ", font=("Arial", 24))
constantes.place(x=10, y=40)
x1 = Label(ventana, text="x1=", font=("Arial", 24))
x1.place(x=10, y=250)
x2 = Label(ventana, text="x2=", font=("Arial", 24))
x2.place(x=10, y=300)
ecuacion = Label(ventana, text="f(x)=ax^2 + bx + c", font=("Arial", 24))
ecuacion.place(x=10, y=350)
a = Entry(ventana, font=("Arial", 24))
a.place(x=80, y=40)
b = Entry(ventana, font=("Arial", 24))
b.place(x=80, y=110)
c = Entry(ventana, font=("Arial", 24))
c.place(x=80, y=200)
boton = Button(
    ventana, text="resolver ecuacion", font=("Arial", 24), command=resolver_ecuacion
)
boton.place(x=10, y=400)
boton2 = Button(
    ventana,
    text="ejemplo raices complejas",
    font=("Arial", 24),
    command=ejemplo_complejos,
)
boton2.place(x=10, y=500)
boton3 = Button(
    ventana, text="ejemplo raices reales", font=("Arial", 24), command=ejemplo_reales
)
boton3.place(x=10, y=600)
boton3 = Button(ventana, text="graficar", font=("Arial", 24), command=graficar)
boton3.place(x=10, y=700)
boton4 = Button(ventana, text="limpiar", font=("Arial", 24), command=limpiar)
boton4.place(x=10, y=800)
fallo = Label(ventana, font=("Arial", 24))
fallo.place(x=600, y=600)
# esta linea siempre va al final
ventana.mainloop()
