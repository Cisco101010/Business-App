import tkinter as tk
from tkinter import messagebox

class SistemaCalculoGastos:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Sistema de Cálculo de Gastos")

        # Configurar el color de fondo de la ventana
        self.ventana.configure(bg="#001F3F")  # Azul oscuro

        # Variables
        self.caja_var = tk.DoubleVar()
        self.gastos_limpieza_var = tk.DoubleVar()
        self.compras_faltantes_var = tk.DoubleVar()
        self.ventas_dia_var = tk.DoubleVar()
        self.total_caja_var = tk.DoubleVar()
        self.total_var = tk.DoubleVar()

        # Etiquetas
        tk.Label(ventana, text="Caja:", bg="#001F3F", fg="white").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        tk.Label(ventana, text="Gastos en productos de limpieza:", bg="#001F3F", fg="white").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        tk.Label(ventana, text="Compras faltantes B/A:", bg="#001F3F", fg="white").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        tk.Label(ventana, text="Ventas del día:", bg="#001F3F", fg="white").grid(row=3, column=0, sticky="w", padx=10, pady=5)
        tk.Label(ventana, text="Total Caja:", bg="#001F3F", fg="white").grid(row=4, column=0, sticky="w", padx=10, pady=5)
        tk.Label(ventana, text="Total:", bg="#001F3F", fg="white").grid(row=5, column=0, sticky="w", padx=10, pady=5)

        # Entradas
        entry_width = 30
        entry_height = 2
        tk.Entry(ventana, textvariable=self.caja_var, width=entry_width, font=("Arial", 20)).grid(row=0, column=1, padx=10, pady=5)
        tk.Entry(ventana, textvariable=self.gastos_limpieza_var, width=entry_width, font=("Arial", 12)).grid(row=1, column=1, padx=10, pady=5)
        tk.Entry(ventana, textvariable=self.compras_faltantes_var, width=entry_width, font=("Arial", 12)).grid(row=2, column=1, padx=10, pady=5)
        tk.Entry(ventana, textvariable=self.ventas_dia_var, width=entry_width, font=("Arial", 12)).grid(row=3, column=1, padx=10, pady=5)
        tk.Entry(ventana, textvariable=self.total_caja_var, state="readonly", width=entry_width, font=("Arial", 12)).grid(row=4, column=1, padx=10, pady=5)
        tk.Entry(ventana, textvariable=self.total_var, state="readonly", width=entry_width, font=("Arial", 12)).grid(row=5, column=1, padx=10, pady=5)

        # Canvas para las barras de progreso
        self.canvas_ventas = tk.Canvas(ventana, width=20, height=0, bg="green")
        self.canvas_ventas.grid(row=9, column=0, columnspan=2, pady=5)

        self.canvas_total_caja = tk.Canvas(ventana, width=20, height=0, bg="white")
        self.canvas_total_caja.grid(row=10, column=0, columnspan=2, pady=5)

        # Botones
        button_width = 20
        button_height = 2

        # Calcular Total
        calcular_button = tk.Button(ventana, text="Calcular Total", command=self.calcular_total, bg="#337AB7", fg="white", borderwidth=2, relief="groove", padx=5, pady=5, bd=2, width=button_width, height=button_height)
        calcular_button.grid(row=0, column=2, padx=(10, 10), pady=5)

        # Cierre
        cerrar_button = tk.Button(ventana, text="Cierre", command=self.cerrar_sistema, bg="#337AB7", fg="white", borderwidth=2, relief="groove", padx=5, pady=5, bd=2, width=button_width, height=button_height)
        cerrar_button.grid(row=1, column=2, padx=(10, 10), pady=5)

        # Actualizar
        actualizar_button = tk.Button(ventana, text="Actualizar", command=self.actualizar_valores, bg="#337AB7", fg="white", borderwidth=2, relief="groove", padx=5, pady=5, bd=2, width=button_width, height=button_height)
        actualizar_button.grid(row=2, column=2, padx=(10, 10), pady=5)

    def calcular_total(self):
        try:
            caja = self.caja_var.get()
            gastos_limpieza = self.gastos_limpieza_var.get()
            compras_faltantes = self.compras_faltantes_var.get()
            ventas_dia = self.ventas_dia_var.get()

            # Calcular el total en caja restando los gastos en productos de limpieza
            total_caja = round(caja - gastos_limpieza - compras_faltantes, 2)

            # Sumar el total en caja con las ventas del día
            total = round(total_caja + ventas_dia, 2)

            # Actualizar las variables de los Entry
            self.total_caja_var.set(total_caja)
            self.total_var.set(total)

            # Crear barras de progreso solo después de calcular la venta
            self.canvas_ventas.config(height=ventas_dia)
            self.canvas_total_caja.config(height=total_caja)

            # Actualizar barras de progreso (velas japonesas)
            self.actualizar_barras_progreso(ventas_dia, total_caja)

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

    def cerrar_sistema(self):
        self.ventana.destroy()

    def actualizar_valores(self):
        # Método para restablecer todos los valores a 0
        self.caja_var.set(0)
        self.gastos_limpieza_var.set(0)
        self.compras_faltantes_var.set(0)
        self.ventas_dia_var.set(0)
        self.total_caja_var.set(0)
        self.total_var.set(0)

        # Restablecer barras de progreso (velas japonesas)
        self.actualizar_barras_progreso(0, 0)

    def actualizar_barras_progreso(self, ventas_dia, total_caja):
        # Limpiar el canvas antes de dibujar nuevas barras de progreso
        self.canvas_ventas.delete("all")
        self.canvas_total_caja.delete("all")

        # Dibujar barras de progreso para las ventas del día
        self.dibujar_barra_progreso(self.canvas_ventas, ventas_dia, "green")

        # Dibujar barras de progreso para el total en caja
        self.dibujar_barra_progreso(self.canvas_total_caja, total_caja, "red")

    def dibujar_barra_progreso(self, canvas, valor, color):
        canvas_width = 20
        canvas_height = 150

        # Ajustar el valor para que esté en el rango de 0 a canvas_height
        valor_ajustado = min(max(valor, 0), canvas_height)

        # Dibujar la barra de progreso
        canvas.create_rectangle(
            canvas_width // 2 - 5,
            canvas_height - valor_ajustado,
            canvas_width // 2 + 5,
            canvas_height,
            fill=color
        )

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = SistemaCalculoGastos(ventana_principal)
    ventana_principal.mainloop()
