from time import sleep
from analog_sensor import read_hume, read_luz
from digital_sensor import read_digital
import threading
import RPi.GPIO as GPIO # type: ignore

def control_luz():
    print("Control de luz iniciado")
    if read_luz() < refLuz:
        toggle(salida[3], 10)
    print("Control de luz terminado")

def control_ambiente():
    print("Control de ambiente iniciado")
    temp, hume = read_digital()
    if hume < refHume:
        toggle(salida[5], 12)
    if temp > 18:
        toggle(salida[4], 12)    
    elif temp < 22:
        toggle(salida[5], 12)
    print("Control de ambiente terminado")

def control_humeSue():
    print("Control de humedad de suelo iniciado")
    sleep(0.1)
    salida = [27, 22, 10]
    hu1, hu2, hu3 = read_hume()
    sensoreHume = [hu1, hu2, hu3]
    for sensor, salida in zip(sensoreHume, salida):
        if sensor < refHumeSue:
            thread_toggle = threading.Thread(target=toggle, args=(salida, 15))
            thread_toggle.start()
            threads.append(thread_toggle)
    for thread_toggle in threads:
        thread_toggle.join()
    print("Control de humedad de suelo terminado")

def toggle(salida, tiempo):
    print(f"Activando salida {salida} por {tiempo} segundos")
    GPIO.output(salida, GPIO.HIGH)
    sleep(tiempo)
    GPIO.output(salida, GPIO.LOW)
    print(f"Salida {salida} desactivada")

def scheduler():
    threads = [
        threading.Thread(target=control_luz,),
        threading.Thread(target=control_humeSue,),
        threading.Thread(target=control_ambiente,)
    ]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

refHume, refHumeSue, refLuz =  70, 32000, 32000
valv1, valv2, valv3, luzArttificial, luzInfraroja, Ventiladores = 27, 22, 10, 9, 11, 5

salida = [valv1, valv2, valv3, luzArttificial, luzInfraroja, Ventiladores]
referencia = [refHume, refHumeSue, refLuz]                         

threat_toggle = threading.Thread(target=toggle)
threads = []

GPIO.setup(valv1, GPIO.OUT)
GPIO.setup(valv2, GPIO.OUT)
GPIO.setup(valv3, GPIO.OUT)
GPIO.setup(luzArttificial, GPIO.OUT)
GPIO.setup(luzInfraroja, GPIO.OUT) 
GPIO.setup(Ventiladores, GPIO.OUT)

if __name__ == "__main__":
   scheduler()