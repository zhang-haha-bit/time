import time  
  
while True:  
    current_time = time.strftime("%H:%M:%S")  
    print(current_time, end="\r", flush=True)  
    time.sleep(1)
