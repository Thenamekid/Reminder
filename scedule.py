import datetime
# import time

while True:
    starting_time = input("What is the starting time of the event(like 06:10)? ")
    # ending_time = input("What is the ending time of the event (like 15:23)? ")
    name = input("What is the name of the event? ")
    
    print("So the name of the event is:", name,"and it is starting at:", starting_time)
    
    current_time = datetime.datetime.now()
    timeFR = current_time.strftime("%H:%M")
    print("Current time:", timeFR)
    
    while timeFR < starting_time:
        # print("Waiting...")
        # print("real time:", timeFR)
        # print("starting time:", starting_time)
        # time.sleep(5)
        
        current_time = datetime.datetime.now()
        timeFR = current_time.strftime("%H:%M")
        
        if timeFR == starting_time:
            print("Event:", name, "is starting!")
            break
    else:
        print("time has passed")