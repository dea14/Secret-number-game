def make_bricks(small, big, goal):
    if goal%5 == big:
       return True
    else:
        if goal%5 >= small:
            return True
        else:
            return False