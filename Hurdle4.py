def turn_right():
    turn_left()
    turn_left()
    turn_left() 

def keep_going():
    while at_goal() != True:
        while wall_on_right() == True and wall_in_front() != True:
            move()
        if wall_on_right() == True and wall_in_front() == True:
            turn_left()
        elif wall_on_right() != True:
            turn_right()
            move()
            turn_right()
            move()

keep_going()