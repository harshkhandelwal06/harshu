print("start a countdown program")
import time
start_time=int(input("enter a number of the second "))
for i in range(start_time,-1,-1):
    print(i)
    time.sleep(1)
print("boost the rocket ")