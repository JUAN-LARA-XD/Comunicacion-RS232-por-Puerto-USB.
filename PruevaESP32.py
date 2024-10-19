import tkinter as GUI
import serial 
import time 


ventana = GUI.Tk()
ventana.title('ESP32')
arduino= None


def CONECTAR():
    global arduino
    print("Función conectar")
    PUERTO = entryCOM.get()  # Obtener el puerto del campo de entrada
    try:
        arduino = serial.Serial(port=PUERTO, baudrate=115200, timeout=.1)  # Configurar el puerto
        print(f"Conectado al puerto {PUERTO}")
    except serial.SerialException:
        print(f"No se pudo conectar al puerto {PUERTO}")

def SEND():
    global arduino
    if arduino and arduino.is_open:
        print("Función envío de datos")
        x = SpinDATA.get()  # Obtener el dato del Spinbox
        arduino.write(bytes(f"{x}\n", 'utf-8'))  # Enviar el dato al Arduino
        time.sleep(0.05)  # Esperar un momento para recibir respuesta
        data = arduino.readline().decode('utf-8').strip()  # Leer la respuesta
        LabelRECIVE.config(text=f"Dato recibido = {data}")  # Mostrar el dato recibido
    else:
        print("Arduino no conectado")

def CERRAR():
    global arduino
    print("Cerrando la aplicación")
    if arduino and arduino.is_open:
        arduino.close()  # Cerrar el puerto serial
        print("Conexión cerrada")
    ventana.quit()  # Cerrar la ventana

# Definir la interfaz
labelCOM_NAME = GUI.Label(ventana, text="Escribe el número del puerto; Ejem: COM3")
entryCOM = GUI.Entry(ventana)
BotonCONECT = GUI.Button(ventana, text="CONECTAR", command=CONECTAR)

SpinDATA = GUI.Spinbox(ventana, from_=0, to=100)
BotonSEND = GUI.Button(ventana, text="ENVIAR", command=SEND)

LabelRECIVE = GUI.Label(ventana, text="Dato recibido =")
BotonCerrar = GUI.Button(ventana, text="SALIR", command=CERRAR)

# Organizar los widgets en la ventana
labelCOM_NAME.pack(padx=1, pady=2)
entryCOM.pack(padx=1, pady=2)
BotonCONECT.pack(padx=1, pady=2)
SpinDATA.pack(padx=1, pady=2)
BotonSEND.pack(padx=1, pady=2)
LabelRECIVE.pack(padx=1, pady=2)
BotonCerrar.pack(padx=1, pady=2)

ventana.mainloop()