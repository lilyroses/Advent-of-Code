n = 100
allocs = []



for a in range(n+1):  # a (0, 11)
    for b in range(n - a + 1): # b (0, 1)
        for c in range(n - a - b + 1):  # c (0, 1)
            d = n - a - b - c  # d = 10 - 0 - 0 - 0 = 10
            allocs.append([a,b,c,d])


for a in range(n + 1):  # a = 0-10
    for b in range((n - a) + 1):  # n - a 
        for c in range((n - a - b) + 1):
        


for alloc in allocs[:300]:

    print(alloc)

