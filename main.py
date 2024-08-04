import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Criar a janela principal
root = tk.Tk()
root.title("Barra de Progreso con Imagen de Fondo")

# Cargar la imagen de fondo
background_image_path = 'sus.jpg'  # Asegúrate de que esta ruta sea correcta
background_image = Image.open(background_image_path)
bg_image_tk = ImageTk.PhotoImage(background_image)

# Crear un widget de canvas para colocar la imagen de fondo
canvas = tk.Canvas(root,
                   width=background_image.width,
                   height=background_image.height)
canvas.pack(fill="both", expand=True)

# Colocar la imagen en el canvas
canvas.create_image(0, 0, image=bg_image_tk, anchor='nw')

# Crear la barra de progreso
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root,
                               variable=progress_var,
                               maximum=100,
                               length=300,
                               mode='determinate')
progress_bar.place(x=background_image.width // 2 - 150,
                   y=background_image.height // 2 -
                   10)  # Ajustar posição segundo a imagem

# Estilo para a barra de progresso
style = ttk.Style()
style.configure("red.Horizontal.TProgressbar",
                background='yellow',
                troughcolor='lightgrey',
                bordercolor='lightgrey')

progress_bar.config(style="red.Horizontal.TProgressbar")


# Função para atualizar a barra de progresso
def update_progress(current_value):
    if current_value <= 100:
        progress_var.set(current_value)
        progress_bar['value'] = current_value
        root.after(10, update_progress,
                   current_value + 1)  # Atualiza a cada 10 ms


# Função para iniciar o progresso
def start_progress():
    progress_var.set(0)  # Reiniciar o progresso
    progress_bar['value'] = 0
    update_progress(0)


# Botão para iniciar o progresso
start_button = tk.Button(root,
                         text="Iniciar",
                         command=start_progress,
                         bg='lightgrey')
start_button.place(x=background_image.width // 2 - 30,
                   y=background_image.height // 2 +
                   20)  # Ajustar posição segundo a imagem

# Executar a aplicação
root.mainloop()
