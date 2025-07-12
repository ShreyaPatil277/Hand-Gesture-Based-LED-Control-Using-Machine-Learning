import pyfirmata

comport='COM3'

board=pyfirmata.Arduino(comport)


led_1=board.get_pin('d:8:o')
led_2=board.get_pin('d:9:o')
led_3=board.get_pin('d:10:o')
led_4=board.get_pin('d:11:o')
led_5=board.get_pin('d:12:o')

def led(fingerUp):
    for i in range(5):
        led_pins[i].write(fingerUp[i])
