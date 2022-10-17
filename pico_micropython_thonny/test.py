import machine


# GPIO pin 28 is used
led_breadboard = machine.Pin(28, machine.Pin.OUT)


while True:
    led_breadboard.value(1)
    led_breadboard.value(0)


