'''def make_bricks(small, big, goal):
    if 5 * big == goal:
        return True
    elif 1 * small == goal:
        return True
    elif (5 * big) > goal and ((5 * big) - goal) >= small:
        return True
    else:
        (5 * big) < goal and (goal - (5 * big)) >= small
        return True


print(make_bricks(3,1,9))'''


def lone_sum(a, b, c):
    if a != b and a != c and b != c:
        return a + b + c
    elif a != b and a=c:
        return b
    elif b != a and b=c:
        return a



