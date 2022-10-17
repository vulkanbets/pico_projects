from machine import Pin, PWM



pwm28 = PWM( Pin(28) )    # create PWM object from a pin
# pwm28.freq()            # get current frequency
pwm28.freq( 100000 )      # set frequency
# pwm28.duty_u16()        # get current duty cycle, range 0-65535
pwm28.duty_u16( 32767 )   # set duty cycle, range 0-65535
# pwm28.deinit()          # turn off PWM on the pin





