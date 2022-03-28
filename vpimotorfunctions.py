def calculateStepsDestination(destination, direction, over=0) 
    
    steps = 0

    if direction == 1:
        #CW
        if destination > POS:
            steps = destination - POS
        elif destination < POS
            steps = 360 - POS + destination 
        elif destination == POS
            steps = 0
            
    elif direction = 0:
        # CCW
        if destination > POS:
            steps = 360 - destination + POS
        elif destination < POS
            steps = POS - destinatin
        elif destination == POS
            steps = 0
    
    # Drüberdrehen wie oft         
    if over != 0:
        steps = steps + over * 360
