from pyb import I2C
from pyb import delay
from array import array

i2c = I2C(1)    #Se crea el objeto i2c, del bus principal del microcontrolador
i2c.init(I2C.MASTER, baudrate = 100000) #se inicia el bus de datos a 10 Khz

class AK8975:   #Se crea la clase AK8975

    def init():
        i2c.mem_write(0b00000010, 0x68, 0x37)   #Se activa el bypass del MPU6050
        i2c.mem_write(0b00000000, 0x68, 0x6B)   #Se define la frecuencia de oscilacion a 8 Mhz

    def get_x():
        datos = array('B', [0] * 2)

        #ID del magnetometro 12
        i2c.mem_write(0b00000001, 0x0C, 0x0A)   #Se establece el modo de operacion "Single measurement mode"
        delay(10)
        datos = i2c.mem_read(2, 0x0C, 0x03)  #Se leen 2 bytes del magnetometro correspondientes al eje x 
        eje_x = (datos[1] << 8) | datos[0]  #Se concatenan los bytes LSB y MSB del eje x

        #Dividir en +180° y -180° el eje x
        if (eje_x > +32768):
            eje_x = eje_x -65536
            

        return(eje_x)

    def get_y():
        datos = array('B', [0] * 2)

        i2c.mem_write(0b00000001, 0x0C, 0x0A)   #Se establece el modo de operacion "Single measurement mode"
        delay(10)
        datos = i2c.mem_read(2, 0x0C, 0x05)   #Se leen 2 bytes del magnetometro correspondientes al eje y
        eje_y = (datos[1] << 8) | datos[0]    #Se concatenan los bytes LSB y MSB del eje y

        #Dividir en +180° y -180° el eje y
        if (eje_y > 32768):
            eje_y = eje_y -65536
            
        return(eje_y)

    