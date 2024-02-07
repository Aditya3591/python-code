import time

class stopwatch:

    def __init__(self):
        self.start_time=0
        self.end_time=0

    def start(self):
        self.start_time=time.time()

    def end(self):
        self.end_time=time.time()

    def elapsed_time(self):
        return  self.end_time-self.start_time
    
obj=stopwatch()

input("enter to start the time")
obj.start()

input("enter to end the time")
obj.end()

print(f"the elapsed time is {obj.elapsed_time()}")