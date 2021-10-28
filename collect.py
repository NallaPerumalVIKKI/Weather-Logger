from sense_hat import * 
from time import sleep
sense= SenseHat()

while True:
 sleep (5)
 myfile= open('weather.txt', 'a')
 myfile.write(sense.temp)
 myfile.write('\n') 
 myfile.close()
