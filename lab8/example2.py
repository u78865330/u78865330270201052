def is_prime(a):
  e = 0
  if a<2:
    return False
  for q in range(2,a):
    if a % q == 0:
      e+=1
  if e >0:
    return False
  else:
    return True

  
  