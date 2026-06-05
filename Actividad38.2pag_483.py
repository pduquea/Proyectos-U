
import math
import tkinter as tk
class CalculadoraNotas:

    def __init__(self, notas):
        self.notas = notas
    def calcular_promedio(self):
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)
    def calcular_desviacion(self):
        if not self.notas:
            return 0.0
        promedio = self.calcular_promedio()
        varianza = sum((nota - promedio) ** 2 for nota in self.notas) / len(self.notas)
        return math.sqrt(varianza)
    def obtener_mayor(self):
        if not self.notas:
            return 0.0
        return max(self.notas)
    def obtener_menor(self):
        if not self.notas:
            return 0.0
        return min(self.notas)
class InterfazNotas:

    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Notas")
        self.root.configure(bg="#FFF5E1")
        self.root.update_idletasks()
        ancho = 420
        alto = 620
        x = (self.root.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.root.winfo_screenheight() // 2) - (alto // 2)
        self.root.geometry(f"{ancho}x{alto}+{x}+{y}")
        self.root.resizable(False, False)
        self.header_bg = "#134E4A"
        self.card_bg = "#FFFFFF"
        self.input_bg = "#EFF6FF"
        self.input_fg = "#0F172A"
        self.highlight_bg = "#93C5FD"
        self.highlight_color = "#2563EB"
        self.primary_bg = "#1E40AF"
        self.primary_hover_bg = "#1D4ED8"
        self.secondary_bg = "#DBEAFE"
        self.secondary_hover_bg = "#BFDBFE"
        self.error_fg = "#B91C1C"
        self.result_bg = "#ECFCCB"
        self.result_fg = "#166534"
        self.label_fg = "#1F2937"
        self.cantidad_notas = 5
        self.cantidad_var = tk.IntVar(value=self.cantidad_notas)
        self.crear_widgets()
    def crear_widgets(self):
        header_frame = tk.Frame(self.root, bg=self.header_bg, pady=15)
        header_frame.pack(fill="x", side="top")
        lbl_titulo = tk.Label(
            header_frame,
            text="Calculadora de Notas",
            font=("Segoe UI", 16, "bold"),
            bg=self.header_bg,
            fg="#F8FAFC"
        )
        lbl_titulo.pack()
        self.lbl_subtitulo = tk.Label(
            header_frame,
            text=f"Ingrese {self.cantidad_notas} calificaciones de 0.0 a 5.0",
            font=("Segoe UI", 9),
            bg=self.header_bg,
            fg="#D1FAE5"
        )
        self.lbl_subtitulo.pack()
        card = tk.Frame(self.root, bg=self.card_bg, padx=20, pady=18, relief="solid", borderwidth=0)
        card.pack(fill="both", expand=True, padx=15, pady=15)
        config_frame = tk.Frame(card, bg=self.card_bg, pady=5)
        config_frame.pack(fill="x")
        lbl_cantidad = tk.Label(
            config_frame,
            text="Cantidad de notas:",
            font=("Segoe UI", 10),
            bg=self.card_bg,
            fg=self.label_fg
        )
        lbl_cantidad.pack(side="left")
        self.spin_cantidad = tk.Spinbox(
            config_frame,
            from_=1,
            to=30,
            width=3,
            textvariable=self.cantidad_var,
            font=("Segoe UI", 10),
            justify="center",
            relief="solid",
            borderwidth=1
        )
        self.spin_cantidad.pack(side="left", padx=(5, 10))
        btn_actualizar = tk.Button(
            config_frame,
            text="Actualizar",
            font=("Segoe UI", 10, "bold"),
            bg=self.secondary_bg,
            fg="#1E293B",
            activebackground=self.secondary_hover_bg,
            activeforeground="#1E293B",
            relief="flat",
            borderwidth=0,
            cursor="hand2",
            command=self.actualizar_cantidad,
            pady=6
        )
        btn_actualizar.pack(side="left")
        self.inputs_frame = tk.Frame(card, bg=self.card_bg)
        self.inputs_frame.pack(fill="x")
        self.crear_campos_entrada()
        self.lbl_error = tk.Label(
            card,
            text="",
            font=("Segoe UI", 9, "bold"),
            bg=self.card_bg,
            fg=self.error_fg,
            wraplength=340,
            justify="center",
            pady=5
        )
        self.lbl_error.pack(fill="x")
        btn_frame = tk.Frame(card, bg=self.card_bg, pady=10)
        btn_frame.pack(fill="x")
        self.btn_calcular = tk.Button(
            btn_frame,
            text="Calcular Estadísticas",
            font=("Segoe UI", 10, "bold"),
            bg=self.primary_bg,
            fg="#FFFFFF",
            activebackground=self.primary_hover_bg,
            activeforeground="#FFFFFF",
            relief="flat",
            borderwidth=0,
            cursor="hand2",
            command=self.calcular,
            pady=8
        )
        self.btn_calcular.pack(side="left", fill="x", expand=True, padx=(0, 5))
        self.btn_calcular.bind("<Enter>", lambda e: self.btn_calcular.config(bg=self.primary_hover_bg))
        self.btn_calcular.bind("<Leave>", lambda e: self.btn_calcular.config(bg=self.primary_bg))
        self.btn_limpiar = tk.Button(
            btn_frame,
            text="Limpiar",
            font=("Segoe UI", 10, "bold"),
            bg=self.secondary_bg,
            fg="#1E293B",
            activebackground=self.secondary_hover_bg,
            activeforeground="#1E293B",
            relief="flat",
            borderwidth=0,
            cursor="hand2",
            command=self.limpiar,
            pady=8
        )
        self.btn_limpiar.pack(side="right", fill="x", expand=True, padx=(5, 0))
        self.btn_limpiar.bind("<Enter>", lambda e: self.btn_limpiar.config(bg=self.secondary_hover_bg))
        self.btn_limpiar.bind("<Leave>", lambda e: self.btn_limpiar.config(bg=self.secondary_bg))
        self.results_frame = tk.LabelFrame(
            card,
            text=" Resultados Estadísticos ",
            font=("Segoe UI", 10, "bold"),
            bg=self.result_bg,
            fg=self.result_fg,
            relief="solid",
            borderwidth=1,
            padx=15,
            pady=10
        )
        self.results_frame.pack(fill="both", expand=True, pady=(10, 0))
        self.results_frame.grid_columnconfigure(0, weight=1)
        self.results_frame.grid_columnconfigure(1, weight=1)
        self.lbl_promedio = self.crear_label_resultado(self.results_frame, "Promedio:", "0.0", 0, 0)
        self.lbl_desviacion = self.crear_label_resultado(self.results_frame, "Desviación:", "0.0000", 0, 1)
        self.lbl_mayor = self.crear_label_resultado(self.results_frame, "Nota más alta:", "0.0", 1, 0)
        self.lbl_menor = self.crear_label_resultado(self.results_frame, "Nota más baja:", "0.0", 1, 1)
    def crear_label_resultado(self, parent, label_text, default_value, row, column):
        frame = tk.Frame(parent, bg=self.result_bg, pady=4, padx=5)
        frame.grid(row=row, column=column, sticky="nsew", padx=5, pady=5)
        lbl_desc = tk.Label(
            frame,
            text=label_text,
            font=("Segoe UI", 9),
            bg=self.result_bg,
            fg=self.label_fg
        )
        lbl_desc.pack(side="left")
        lbl_val = tk.Label(
            frame,
            text=default_value,
            font=("Segoe UI", 10, "bold"),
            bg=self.result_bg,
            fg="#0F172A"
        )
        lbl_val.pack(side="right")
        return lbl_val
    def crear_campos_entrada(self):
        for widget in self.inputs_frame.winfo_children():
            widget.destroy()
        self.entradas_notas = []
        for i in range(self.cantidad_notas):
            row_frame = tk.Frame(self.inputs_frame, bg=self.card_bg, pady=5)
            row_frame.pack(fill="x")
            lbl = tk.Label(
                row_frame,
                text=f"Nota {i+1}:",
                font=("Segoe UI", 10),
                bg=self.card_bg,
                fg=self.label_fg,
                width=10,
                anchor="w"
            )
            lbl.pack(side="left")
            entry = tk.Entry(
                row_frame,
                font=("Segoe UI", 10),
                bg=self.input_bg,
                fg=self.input_fg,
                relief="solid",
                borderwidth=1,
                highlightthickness=0
            )
            entry.config(highlightbackground=self.highlight_bg, highlightcolor=self.highlight_color)
            entry.pack(side="left", fill="x", expand=True, ipady=3)
            self.entradas_notas.append(entry)
    def actualizar_cantidad(self):
        try:
            cantidad = int(self.cantidad_var.get())
        except (ValueError, tk.TclError):
            cantidad = self.cantidad_notas
        cantidad = max(1, min(30, cantidad))
        self.cantidad_notas = cantidad
        self.lbl_subtitulo.config(text=f"Ingrese {cantidad} calificaciones de 0.0 a 5.0")
        self.crear_campos_entrada()
    def validar_notas(self):
        notas = []
        for i, entry in enumerate(self.entradas_notas):
            valor_texto = entry.get().strip()
            if not valor_texto:
                raise ValueError(f"Error: La Nota {i+1} está vacía. Complete todas las notas.")
            valor_texto = valor_texto.replace(",", ".")
            try:
                nota = float(valor_texto)
            except ValueError:
                raise ValueError(f"Error: La Nota {i+1} ('{valor_texto}') no es un número válido.")
            if not (0.0 <= nota <= 5.0):
                raise ValueError(f"Error: La Nota {i+1} ({nota}) debe estar en el rango de 0.0 a 5.0.")
            notas.append(nota)
        return notas
    def calcular(self):
        self.lbl_error.config(text="")
        try:
            notas = self.validar_notas()
            calculadora = CalculadoraNotas(notas)
            self.lbl_promedio.config(text=f"{calculadora.calcular_promedio():.2f}")
            self.lbl_desviacion.config(text=f"{calculadora.calcular_desviacion():.4f}")
            self.lbl_mayor.config(text=f"{calculadora.obtener_mayor():.2f}")
            self.lbl_menor.config(text=f"{calculadora.obtener_menor():.2f}")
        except ValueError as err:
            self.lbl_error.config(text=str(err))
            self.lbl_promedio.config(text="0.0")
            self.lbl_desviacion.config(text="0.0000")
            self.lbl_mayor.config(text="0.0")
            self.lbl_menor.config(text="0.0")
    def limpiar(self):
        for entry in self.entradas_notas:
            entry.delete(0, tk.END)
        self.lbl_error.config(text="")
        self.lbl_promedio.config(text="0.0")
        self.lbl_desviacion.config(text="0.0000")
        self.lbl_mayor.config(text="0.0")
        self.lbl_menor.config(text="0.0")
if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazNotas(root)
    root.mainloop()
