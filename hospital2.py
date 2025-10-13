import threading
import time
import random
#...function 1:reading patient sensor data....
def read_sensor_data():
    for i in range(5):
        heart_rate = random.randint(60,120)
        temperature = round(random.uniform(36.5,39.0),1)
        print(f"[sensor] Reading {i+1}:Heart rate={heart_rate} bpm,Temp={temperature}")
        time.sleep(2)
#...function 2:sending doctor notifications.....
def notify_doctor():
    for i in range(3):
        print(f"[Notification]Doctor notified about patient condition{i+1}")
        time.sleep(3)
#......function 3:Logging data....
def log_data():
  for i in range(4):
   print(f"[logger]Data saved in system log {i+1}")
time.sleep(2.5)
#........creating threads.....
t1=threading.Thread(target=read_sensor_data)
t2=threading.Thread(target=notify_doctor)
t3=threading.Thread(target=log_data)
#.......starting Threads.....
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join() 
print("/n all task are completed")        


