""" ====================================================================================================
Pemrogram      : Kelompok EK-3C/10
  1. 12-Merry Nilna Na'ma      NIM:3.32.19.2.13
  2. 24-Yusron Alfauzi         NIM:3.32.19.2.25
Tgl.Presentasi  : Senin, 17 Januari 2022
=======================================================================================================
ProyekArduino
C10-Door Lock System using Face Recognition
  program untuk membuka kunci otomatis berdasarkan pengenalan wajah berbasis artificial intelligence
-----------------------------------------------------------------------------------------------------"""

from pyfirmata2 import Arduino, SERVO
import time

port = 'COM19'
pin = 10

board=Arduino(port)
board.digital[pin].mode=SERVO

def rotateServo(pin, angle):                # fungsi untuk menentukan pin dan besar putaran sudut servo
    board.digital[pin].write(angle)


def doorAutomate(val):                      # fungsi untuk membuka atau menutup kunci
    if val==0:                              # kunci terbuka
        rotateServo(pin, 50)
        time.sleep(3)
    elif val==1:                            # kunci tertutup
        rotateServo(pin, 150)
