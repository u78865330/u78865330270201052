def get_evens(my_list):
  if len(my_list)==0:
    return []
  else:
    return [my_list[-1]%2]+get_evens(my_list[:-1])
x=get_evens([4,3,2,1,6])
print(x.count(0))



  
  