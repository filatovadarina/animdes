from machine import Pin, Timer, ADC

# Create a digital output pin
led_pin = Pin(5, Pin.OUT)

# Create a timer that triggers a function every 1 second
def toggle_led(timer):
    led_pin.value(not led_pin.value())

timer = Timer(-1)
timer.init(period=1000, mode=Timer.PERIODIC, callback=toggle_led)

# Create an analog input pin
potentiometer_pin = ADC(0)

# Read the analog input value every 500ms
def read_potentiometer(timer):
    value = potentiometer_pin.read()
    print("Potentiometer value:", value)

timer2 = Timer(-1)
timer2.init(period=500, mode=Timer.PERIODIC, callback=read_potentiometer)
