i = 0
while True:
  i += 1
  print(f"Outer while loop: {i}")
  if i > 10:
    for j in range(i, i*i):
      print(f"\tInner for loop: {j}")
      if j == 100:
        print(f"\n\tj = 100; breaking...")
        break
    print(f"breaking while loop")
    break
