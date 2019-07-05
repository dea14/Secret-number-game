def make_bricks(small, big, goal):
   if 5*big == goal:
     return True
   elif 5*big > goal and 5%big >= small:
     return True
   elif 5*big<goal and (goal- 5*big) >= small:
     return True
   else:
     return False

print(make_bricks(3,1,9))