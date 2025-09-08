allocs = []
a,b,c,d = 0,0,0,10
alloc = [a,b,c,d]
allocs.append(alloc)


while d > 0:
  d -= 1
  c += 1
  alloc = [a,b,c,d]
  print(alloc)
