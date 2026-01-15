from tkinter import Tk, Label, Entry, Button, Frame
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Funciones
def ejemplo_reales():
    limpiar()
    a_entry.insert(0, "1")
    b_entry.insert(0, "4")
    c_entry.insert(0, "0")

def ejemplo_complejos():
    limpiar()
    a_entry.insert(0, "1")
    b_entry.insert(0, "2")
    c_entry.insert(0, "6")

def limpiar():
    fallo_label.config(text="")
    a_entry.delete(0, "end")
    b_entry.delete(0, "end")
    c_entry.delete(0, "end")
    x1_label.config(text="x1 =")
    x2_label.config(text="x2 =")

def resolver_ecuacion():
    try:
        var_a = float(a_entry.get())
        var_b = float(b_entry.get())
        var_c = float(c_entry.get())
        discriminante = var_b**2 - 4*var_a*var_c
        if discriminante >= 0:
            rx1 = (-var_b + sqrt(discriminante)) / (2 * var_a)
            rx2 = (-var_b - sqrt(discriminante)) / (2 * var_a)
            x1_label.config(text=f"x1 = {rx1:.3f}")
            x2_label.config(text=f"x2 = {rx2:.3f}")
            fallo_label.config(text="")
        else:
            fallo_label.config(text="Solución compleja")
    except ValueError:
        fallo_label.config(text="Error: Debes poner números")

def graficar():
    try:
        val_a = float(a_entry.get())
        val_b = float(b_entry.get())
        val_c = float(c_entry.get())
    except ValueError:
        val_a, val_b, val_c = 1, 2, 5  # valores por defecto

    x = np.linspace(-10, 10, 400)
    y = val_a * x**2 + val_b * x + val_c

    fig, ax = plt.subplots(figsize=(6, 5), dpi=100)
    ax.plot(x, y, label=f"{val_a}x² + {val_b}x + {val_c}")
    ax.axhline(0, color="black", linewidth=1)
    ax.axvline(0, color="black", linewidth=1)
    ax.set_title("Gráfica")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid(True)
    ax.legend()

    global canvas_widget
    try:
        canvas_widget.destroy()
    except:
        pass

    canvas = FigureCanvasTkAgg(fig, master=frame_graph)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill="both", expand=True)
    canvas.draw()


# Ventana principal
ventana = Tk()
ventana.geometry("950x650")
ventana.title("Sistema para Resolver Ecuaciones Cuadráticas")
ventana.configure(bg="#2c2c2c")  # Fondo oscuro

# Título centrado arriba
titulo = Label(ventana, text="Sistema para Resolver Ecuaciones Cuadráticas", font=("Arial", 16, "bold"), fg="white", bg="#2c2c2c")
titulo.place(relx=0.5, y=10, anchor="n")

# Panel izquierdo para entradas y resultados
panel_izquierdo = Frame(ventana, bg="#2c2c2c")
panel_izquierdo.place(x=20, y=50, width=300, height=500)

Label(panel_izquierdo, text="a =", font=("Arial", 14), fg="white", bg="#2c2c2c").place(x=0, y=0)
Label(panel_izquierdo, text="b =", font=("Arial", 14), fg="white", bg="#2c2c2c").place(x=0, y=50)
Label(panel_izquierdo, text="c =", font=("Arial", 14), fg="white", bg="#2c2c2c").place(x=0, y=100)
Label(panel_izquierdo, text="ax^2 + bx + c = 0", font=("Arial", 14), fg="white", bg="#2c2c2c").place(x=0, y=150)

a_entry = Entry(panel_izquierdo, font=("Arial", 14))
a_entry.place(x=50, y=0, width=200)
b_entry = Entry(panel_izquierdo, font=("Arial", 14))
b_entry.place(x=50, y=50, width=200)
c_entry = Entry(panel_izquierdo, font=("Arial", 14))
c_entry.place(x=50, y=100, width=200)

x1_label = Label(panel_izquierdo, text="x1 =", font=("Arial", 14), fg="white", bg="#2c2c2c")
x1_label.place(x=0, y=200)
x2_label = Label(panel_izquierdo, text="x2 =", font=("Arial", 14), fg="white", bg="#2c2c2c")
x2_label.place(x=0, y=240)

# Panel derecho para gráfica con borde azul
frame_graph = Frame(ventana, bg="#1a1a1a", highlightbackground="blue", highlightthickness=1)
frame_graph.place(x=350, y=50, width=530, height=500)

# Botones abajo en dos filas, centrados respecto al frame de gráfica
boton_graficar = Button(ventana, text="Graficar", font=("Arial", 12), width=12, command=graficar)
boton_zoom_out = Button(ventana, text="Zoom Out", font=("Arial", 12), width=12)
boton_zoom_in = Button(ventana, text="Zoom In", font=("Arial", 12), width=12)

boton_graficar.place(x=360, y=570)
boton_zoom_out.place(x=500, y=570)
boton_zoom_in.place(x=640, y=570)

boton_ejemplo_reales = Button(ventana, text="Ejemplo raíces reales", font=("Arial", 12), width=18, command=ejemplo_reales)
boton_ejemplo_complejos = Button(ventana, text="Ejemplo raíces complejas", font=("Arial", 12), width=20, command=ejemplo_complejos)
boton_resolver = Button(ventana, text="Resolver", font=("Arial", 12), width=12, command=resolver_ecuacion)
boton_limpiar = Button(ventana, text="Limpiar", font=("Arial", 12), width=12, command=limpiar)

boton_ejemplo_reales.place(x=20, y=520)
boton_ejemplo_complejos.place(x=20, y=570)
boton_resolver.place(x=780, y=570)
boton_limpiar.place(x= 230, y=570)

fallo_label = Label(ventana, font=("Arial", 12), fg="red", bg="#2c2c2c")
fallo_label.place(x=20, y=610)

canvas_widget = None

ventana.mainloop()
