from machine import Pin, PWM
import time

# Define the servo pin and PWM frequency
servo_pin = Pin(17)
pwm1 = PWM(servo_pin, freq=50)  # MG996R typically uses 50Hz PWM frequency

def set_servo_speed(speed):
    if speed < -100 or speed > 100:
        raise ValueError("Speed must be between -100 and 100")
    
    # Neutral duty cycle (1.5 ms pulse width)
    neutral_duty = 1.5 / 20.0 * 1023  # 20ms period for 50Hz frequency, scaled to 10-bit
    
    if speed == 0:
        duty = neutral_duty
    elif speed > 0:
        # Speed > 0: forward rotation, increase pulse width
        duty = neutral_duty + (speed / 100.0) * (0.5 / 20.0 * 1023)
    else:
        # Speed < 0: backward rotation, decrease pulse width
        duty = neutral_duty + (speed / 100.0) * (0.5 / 20.0 * 1023)
    
    print(f"Speed: {speed}, Duty Cycle: {int(duty)}")
    pwm1.duty(int(duty))

# Example: Set the servo to rotate forward at full speed
set_servo_speed(100)
time.sleep(2)

# Example: Set the servo to stop
set_servo_speed(0)
time.sleep(2)

# Example: Set the servo to rotate backward at half speed
set_servo_speed(-50)
time.sleep(2)

# Stop the servo
set_servo_speed(0)
pwm1.deinit()  # Deinitialize the PWM to stop the servo


"""
from machine import Pin, SPI
import time

class MAX6675:
    def __init__(self, spi, cs_pin):
        self._spi = spi
        self._cs = Pin(cs_pin, Pin.OUT)
        self._cs.value(1)

    def read(self):
        self._cs.value(0)
        raw = self._spi.read(2)
        self._cs.value(1)
        value = (raw[0] << 8 | raw[1]) >> 3
        if value & 0x800:
            return float('nan'), raw  # Thermocouple disconnected
        return value * 0.25, raw

spi = SPI(1, baudrate=5000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
max6675 = MAX6675(spi, cs_pin=5)

while True:
    temp, raw = max6675.read()
    print("Raw data: {} {} Temperature: {:.2f} °C".format(raw[0], raw[1], temp))
    time.sleep(1)


"""


    
