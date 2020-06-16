import RPi.GPIO as GPIO #외부포트를 설정
import time
pin=25
TRIG = 13
ECHO = 26
GPIO.setmode(GPIO.BCM)# BCM타입을 사용한다고 지정
GPIO.setup(pin, GPIO.OUT)# OUTPUT MODE
GPIO.setup(TRIG, GPIO.OUT)# OUTPUT MODE
GPIO.setup(ECHO, GPIO.IN)# INPUT MODE
GPIO.output(TRIG, GPIO.LOW)# Reset trigger value
p = GPIO.PWM(pin,50)
p.start(0)

def distance_check():
      GPIO.output(TRIG, GPIO.HIGH)# High trigger value
      time.sleep(0.00001) # Send trigger pulse for 10us
      GPIO.output(TRIG, GPIO.LOW)# Reset trigger value
      start=0
      stop=0
      while GPIO.input(ECHO) == GPIO.LOW: # 초음파 전송이 끝나는 전송시간 저장
            start = time.time()
      while GPIO.input(ECHO) == GPIO.HIGH:# 초음파 수신이 완료될때 수신시간
            stop = time.time()
            duration = stop-start # 초음파 수신시간에 전송시간을 빼서 도달 시간을 설정
            distance = (duration*340*100)/2 #
      return distance
try:
      while 1:
            result_distance = distance_check()
            print("distance = %.2f cm" %(result_distance))#  거리를 터미널에 출력            
            p.ChangeDutyCycle(0)
            if result_distance <= 30:
                  p.ChangeDutyCycle(7.5)                  
                  time.sleep(5)
                  p.ChangeDutyCycle(0)
                  p.ChangeDutyCycle(2.5)
            time.sleep(0.0001)
except KeyboardInterrupt :
      GPIO.cleanup()
      p.stop()
























            

            
