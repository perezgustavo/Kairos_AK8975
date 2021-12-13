from kairos_AK8975 import AK8975
from pyb import delay
import math

AK8975.init()   #Se invoca el metodo para iniciar la configuracion

#Obtener la declinacion magnetica en la pagina web https://www.magnetic-declination.com/
declinacion = 0.0668 #declinacion magnetica en radianes

while True:

    x = AK8975.get_x()
    y = AK8975.get_y()

    #Se calcula el angulo del eje x con respecto al norte
    ang_rad = math.atan2(y, x) + declinacion

    #Los valores negativos, se convierten a positivos
    if(ang_rad < 0):
        ang_rad = ang_rad + 2*math.pi
        
    #Se convierte de radianes a grados
    grados = int(ang_rad * 180/math.pi)

    print(grados)

    delay(100)