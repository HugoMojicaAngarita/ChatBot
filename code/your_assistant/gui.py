# gui.py
import tkinter as tk
import customtkinter as ctk
from text_processing import get_answer
from PIL import Image, ImageTk

def exit_app():
    """
    Maneja el evento de salida de la aplicación.
    Cierra la ventana principal y termina el bucle de la interfaz gráfica.
    """
    root.quit()

def setup_ui():
    """
    Configura la interfaz de usuario de la aplicación, incluyendo los componentes de entrada, botones y cuadro de respuesta.
    """
    ctk.set_appearance_mode("light")  # Establece el modo de apariencia de la interfaz
    ctk.set_default_color_theme("blue")  # Establece el tema de color predeterminado

    global root
    root = ctk.CTk()  # Crea la ventana principal de la aplicación
    root.title("Tennis Assistant")  # Establece el título de la ventana
    root.geometry("900x600")  # Define las dimensiones de la ventana
    root.configure(bg="#c2bbb8")  # Configura el color de fondo de la ventana

    # Cargar y mostrar la imagen al costado izquierdo
    image_path = "images/image.jpg"  # Ruta a tu imagen
    image = Image.open(image_path)
    image = image.resize((400, 750))  # Ajusta el tamaño según sea necesario

    # Mantener la referencia de la imagen globalmente
    global image_tk
    image_tk = ImageTk.PhotoImage(image)

    # Frame para la imagen
    image_frame = ctk.CTkFrame(root)
    image_frame.pack(side="left", fill="y")
    
    # Label para mostrar la imagen
    image_label = ctk.CTkLabel(image_frame, text="", image=image_tk)
    image_label.pack(side="left", fill="y")

    # Frame para el contenido de texto y entrada
    content_frame = ctk.CTkFrame(root, fg_color="#c2bbb8")
    content_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

    global response_box
    response_box = ctk.CTkTextbox(content_frame, wrap=ctk.WORD, width=400, height=200, font=ctk.CTkFont(size=15))  # Cuadro de texto para mostrar las respuestas
    response_box.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)  # Agrega el cuadro de texto al frame de contenido
    response_box.tag_config("user", foreground="#451e0c")  # Configura el estilo del texto del usuario
    response_box.tag_config("assistant", foreground="#000000")  # Configura el estilo del texto del asistente

    # Marco para alinear el campo de entrada y el botón horizontalmente
    input_frame = ctk.CTkFrame(content_frame, fg_color="#c2bbb8")  # Marco para contener la entrada y el botón
    input_frame.pack(padx=10, pady=10, fill=tk.X)  # Agrega el marco a la ventana principal

    global question_entry
    question_entry = ctk.CTkEntry(input_frame, width=400, font=ctk.CTkFont(size=14), placeholder_text="Ask a question...")  # Campo de entrada para preguntas del usuario
    question_entry.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill=tk.X)  # Agrega el campo de entrada al marco, alineado a la izquierda

    ask_button = ctk.CTkButton(input_frame, text="Ask", command=lambda: get_answer(question_entry, response_box), 
                               font=ctk.CTkFont(size=14), fg_color="#c2d9ff", text_color="#051e47")  # Botón para enviar la pregunta
    ask_button.pack(side=tk.LEFT, padx=5)  # Agrega el botón al marco, alineado a la derecha del campo de entrada

    exit_button = ctk.CTkButton(content_frame, text="Quit", command=exit_app, font=ctk.CTkFont(size=14), fg_color="transparent",
                                text_color="#051e47", border_color="#051e47", border_width=2)  # Botón para salir de la aplicación
    exit_button.pack(pady=5)  # Agrega el botón de salida al frame de contenido

def main():
    """
    Punto de entrada principal para la interfaz gráfica. Configura la interfaz y ejecuta el bucle principal.
    """
    setup_ui()  # Configura la interfaz de usuario
    root.mainloop()  # Inicia el bucle principal de la interfaz gráfica

if __name__ == "__main__":
    main()  # Ejecuta la función principal si este archivo se ejecuta directamente
