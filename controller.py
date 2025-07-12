
import pyfirmata

comport = 'COM5'  # Change to your actual COM port
board = pyfirmata.Arduino(comport)

# Define LED pins (digital 8–12)
led_pins = [board.get_pin(f'd:{i}:o') for i in [8, 9, 10, 11, 12]]

def led(fingerUp):
    # Safely handle if fingerUp is not 5 elements
    if len(fingerUp) != 5:
        print("Invalid finger pattern:", fingerUp)
        return
    
    print("Finger Pattern:", fingerUp)
    for i in range(5):
        led_pins[i].write(fingerUp[i])
