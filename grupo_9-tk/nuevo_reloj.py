import tkinter as tk
import time

def hora(ventana):
    ventana.title('Reloj simple')
    ventana.geometry('400x200')
    reloj = tk.Label(ventana, font = ('Arial', 60), bg = 'blue', fg = 'white')
    def mostrar_reloj():
        hora_actual = time.strftime('%H:%M:%S')
        reloj.config(text=hora_actual)
        reloj.after(1000, mostrar_reloj)

    ventana.after(100, mostrar_reloj)
    reloj.pack(anchor = 'center')


if __name__ == "__main__":
    ventana=tk.Tk()
    hora(ventana)
    ventana.mainloop()
    
