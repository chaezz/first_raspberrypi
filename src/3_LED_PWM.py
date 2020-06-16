import RPi.GPIO as GPIO #외부포트를 설정
import time # 시간함수(지연시간을 설정할 때 사용하는 함수)
LED = 12
a=0 #duty cycle 0%
GPIO .setmode(GPIO.BCM)# BCM타입을 사용한다고 지정
GPIO .setup(LED, GPIO.OUT)# OUTPUT MODE
pwm=GPIO.PWM(LED,5000) #
pwm.start(0) #0% output start

try:
      
      while a < 100:
            pwm.ChangeDutyCycle(a) # pwm signal
            time.sleep(0.5) #delay 0.5 second
            a+=50
            print(a)
            if a==100:
                  GPIO.cleanup()#GPIO port close   
                  #pwm.stop()                  
except KeyboardInterrupt:      
      pwm.stop()# pwm stop[Ctrl+c]
      GPIO.cleanup()#GPIO port close      



            
