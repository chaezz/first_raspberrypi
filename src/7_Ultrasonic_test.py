import lcddriver #chmod set all usable
import RPi.GPIO as GPIO #외부포트를 설정
import time

GPIO.setmode(GPIO.BCM)# BCM타입을 사용한다고 지정
TRIG = 13
ECHO = 26
GPIO.setup(TRIG, GPIO.OUT)# OUTPUT MODE
GPIO.setup(ECHO, GPIO.IN)# INPUT MODE
GPIO.output(TRIG, GPIO.LOW)# Reset trigger value
display = lcddriver.lcd()


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
            display.lcd_display_string("dist.= %.2f cm" %(result_distance),1)
            time.sleep(0.5)
            display.lcd_clear()
except KeyboardInterrupt :
      display.lcd_clear()
      GPIO.cleanup()

























            

            
