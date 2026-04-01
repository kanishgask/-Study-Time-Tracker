import time

def start_timer(seconds):
    print("Study timer started...")
    
    for i in range(seconds, 0, -1):
        print("Time left:", i, "seconds")
        time.sleep(1)
        
    print("Time's up! Study session completed.")
