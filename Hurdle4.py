def turn_right():
    turn_left()
    turn_left()
    turn_left()   
        
def big_jump():
    turn_left()
    move()
    turn_right()

def keep_going():
    if wall_in_front() == True:
        big_jump()
    else:
        move()
    
while at_goal() != True:
    keep_going()