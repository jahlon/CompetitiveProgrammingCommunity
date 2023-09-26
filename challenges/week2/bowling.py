import sys

with sys.stdin as stdin:
    line = stdin.readline()
    while line != "Game Over\n":
        rolls = line.split()
        score = 0
        frames = 0
        i_ant = 20
        for i in range(len(rolls)):
            if frames == 10:
                break
            roll = rolls[i]

            if roll == "X":
                score += 10
                if i + 1 < len(rolls):
                    if rolls[i+1] == "X":
                        score += 10
                        if i + 2 < len(rolls):
                            if rolls[i+2] == "X":
                                score += 10
                            else:
                                score += int(rolls[i+2])
                    else:
                        if rolls[i+2] == "/":
                            score += 10
                        else:
                            score += int(rolls[i+1]) + int(rolls[i+2])
                frames += 1
            elif roll == "/":
                score += 10 - int(rolls[i-1])
                if i + 1 < len(rolls):
                    if rolls[i+1] == "X":
                        score += 10
                    else:
                        score += int(rolls[i+1])
                frames += 1
            else:
                score += int(roll)
                if i_ant == i-1:
                    frames += 1
                    i_ant = 0
                else:
                    i_ant = i

        print(score)
        line = stdin.readline()
