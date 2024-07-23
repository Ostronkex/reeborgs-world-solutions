def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()    
    
def keep_going():
    if wall_in_front() == True:
        jump()
    else:
        move()
        
while at_goal() != True:
    keep_going()
