    #The functions move() and turn_left().
    #Either the test front_is_clear() or wall_in_front(), right_is_clear() or wall_on_right(), and at_goal().
    #How to use a while loop and if/elif/else statements.
    #It might be useful to know how to use the negation of a test (not in Python).

#move()
#turn_left()
#front_is_clear()
#right_is_clear()
#at_goal()
#while loops and if/elif/else

#move()
#turn_left()
#front_is_clear()
#right_is_clear()
#at_goal()
#while loops and if/elif/else

def turn_right():
    turn_left()
    turn_left()
    turn_left() 

def keep_going():
    while at_goal() != True:
        if wall_in_front() == True:
            turn_left()
        while wall_on_right() == True and wall_in_front() != True:
            move()
        while front_is_clear():
            move()
        if right_is_clear() == True and at_goal() != True:
            turn_right()
            move()
            turn_right()

keep_going()


