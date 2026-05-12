n = 5

for i in range(1,4):
    print(f"({i}+1) % {n} = {(i+1)%n}")

for i in range(1,4):
    print(f"{n} % ({i}+1) = {n%(i+1)}")
