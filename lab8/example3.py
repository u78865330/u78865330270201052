def decimal_to_binary(a):
  if a == 1:
      print("1")
  w = ""
  
  while a > 0:
    if a%2 == 1:
      w+="1"
    else:
      w+="0"
    a = a//2
  
  return w[::-1]