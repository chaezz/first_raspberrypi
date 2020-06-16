import lcddriver #chmod set all usable
import RPi.GPIO as GPIO #외부포트를 설정
import time # 시간함수(지연시간을 설정할 때 사용하는 함수)
import Adafruit_DHT

GPIO .setmode(GPIO.BCM)# BCM타입을 사용한다고 지정
sensor = Adafruit_DHT.DHT22
pin = 23
display = lcddriver.lcd()


try:      
      while True:
            humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)           
            if humidity is not None and temperature is not None:
                display.lcd_display_string('Temp. : {0:0.1f} C' .format(temperature),1)
                display.lcd_display_string('Humidity: {0:0.1f} %' .format(humidity),2)
            else:    
                print('Failed to get reading. Try again!')    
except KeyboardInterrupt:
      display.lcd_clear()
      GPIO.cleanup()#GPIO port close      



            
