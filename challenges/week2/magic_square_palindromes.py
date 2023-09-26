import sys
from math import sqrt

with sys.stdin as stdin:
    t = int(stdin.readline())
    result = ''
    for i in range(t):
        line = stdin.readline()
        line = ''.join(map(str, filter(lambda x: x not in ".,?!() \n", line)))
        if line[::-1] == line:
            n = int(sqrt(len(line)))
            if n*n == len(line):
                result += f"Case #{i+1}:\n"
                result += f"{n}\n"
            else:
                result += f"Case #{i+1}:\n"
                result += "No magic :(\n"
        else:
            result += f"Case #{i + 1}:\n"
            result += "No magic :(\n"

    print(result[:-1])
