def selection_sort(lst):
  n = len(lst)
  for bottom in range(n-1):
    mp = bottom
    for i in range(bottom+1,n):
      if lst[i]<lst[mp]:
        mp+=1
    lst[n],lst[mp]=lst[mp],lst[n]
  return lst