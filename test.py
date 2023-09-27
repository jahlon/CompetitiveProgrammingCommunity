import random
print("1")
print("100 100 100")
for _ in range(100):
    for _ in range(100):
        if random.randint(0, 1) == 0:
            print("S", end="")
        else:
            print("R", end="")
    print()
