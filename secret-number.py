def make_bricks(small, big, goal):
    if 5 * big == goal:
        return True
    elif 1 * small == goal:
        return True
    elif (5 * big) > goal and ((5 * big) - goal) >= small:
        return True
    else:
        (5 * big) < goal and (goal - (5 * big)) >= small
        return True


print(make_bricks(3,1,9))

