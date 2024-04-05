def turn_right():
    turn_left()
    turn_left()
    turn_left()
   
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for step in range(6):
    jump()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()