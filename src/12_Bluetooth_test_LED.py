import bluetooth
import RPi.GPIO as GPIO 

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

port = 1

server_socket.bind(("",port))

server_socket.listen(1)
client_socket, address = server_socket.accept()
print("Accepted connection from", address)


try :            
      while 1:
            data = client_socket.recv(1024)
            print("Received: %s" % data)
            if data == "R":
                  GPIO.output(26, True)
                  GPIO.output(19, False)
                  GPIO.output(13, False)
            if data == "G":
                  GPIO.output(19, True)
                  GPIO.output(26, False)
                  GPIO.output(13, False)
            if data == "B":
                  GPIO.output(13, True)
                  GPIO.output(19, False)
                  GPIO.output(26, False)
            if data == "Q":
                  print("Quit")
                  break
            if data == "OFF":
                  GPIO.output(19, False)
                  GPIO.output(26, False)
                  GPIO.output(13, False)    

except KeyboardInterrupt:
      GPIO.cleanup()#GPIO port close            
      client_socket.close()
      server_socket.close()
                        
