def cigar_party(cigars, is_weekend):
  if cigars >= 40 and cigars <= 60 or is_weekend == True:
    return True 
  elif cigars >= 40 or is_weekend == True:
    return True
  else:
    return False
print((cigar_party(20, True)))



def date_fashion(you, date):
    if you >= 8:
        if date > 2:
            return 2
        else:
            return 0
    elif date >= 8:
        if you > 2:
            return 2
        else:
            return 0
    elif you <= 2 and you < 8 and date <= 2 and date < 0:
        return 0
    else:
        return 1

print(date_fashion(3,7))

