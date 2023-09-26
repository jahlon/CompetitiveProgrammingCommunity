import math

n = int(input())

names = []
song = ["Happy", "birthday", "to", "you"] * 2
song += ["Happy", "birthday", "to", "Rujia"] * 2
song[-1] = "you"


if n > 16:
    reps = math.ceil(n / 16)
    song *= reps


for _ in range(n):
    names.append(input())


for i in range(len(song)):
    print(f'{names[i % n]}: {song[i]}')   
