import lcddriver #chmod set all useable
import RPi.GPIO as GPIO #외부포트를 설정
import time # 시간함수(지연시간을 설정할 때 사용하는 함수)
import Adafruit_DHT
GPIO .setmode(GPIO.BCM)# BCM타입을 사용한다고 지정
GPIO .setup(16, GPIO.OUT)# OUTPUT MODE
GPIO .setup(25, GPIO.IN)# OUTPUT MODE

display = lcddriver.lcd()


try:      
      while True:
            if GPIO.input(25)==True:
                GPIO.output(16, True)
                display.lcd_display_string("LED On!!", 1)
                print("Switch On!!")
            else:
                GPIO.output(16, False)               
                display.lcd_display_string("LED OFF!!", 1)
                print("Switch OFF!!")
except KeyboardInterrupt:
      display.lcd_clear()
      GPIO.cleanup()#GPIO port close      



            
