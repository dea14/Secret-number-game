def make_chocolate(small, big, goal):
  if (5*big)+(1*small)==goal:
    return small
  elif (5*big) == goal:
    return 0
  elif (5*big) > goal and (goal-(5*big))%5 == 0:
    return 0
  elif (5*big) < goal and (1*small) == goal:
    return small
  elif (5*big) < goal and (goal-(5*big)) < small:
    return small - (goal-(5*big)
  else:
    return -1




