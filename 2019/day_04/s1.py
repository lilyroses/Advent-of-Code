INPUT_FILE = "input.txt"
with open(INPUT_FILE, 'r') as f:
    lines = [line.strip() for line in f.readlines()]


x, y = [int(n) for n in lines[0].split('-')]

n = x

def is_valid(n):
    ds = []
    has_pair = False

    pd = n % 10
    n = n//10
    ds = [pd]

    while n > 0:
        d = n%10
        n = n//10
        if d == pd:
            has_pair = True
        if d <= pd:
            ds.append(d)
            pd = d
        else:
            return False
    return has_pair


t = 0
for n in range(x, y+1):
    if is_valid(n):
        t+= 1

print(t)
