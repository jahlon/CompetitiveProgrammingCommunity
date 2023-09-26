import sys


counter = 0
with sys.stdin as stdin:
    ch = stdin.read(1)
    while ch:        
        if ch == '"':
            counter += 1
            if counter % 2 == 1:
                sys.stdout.write('``')
            else:
                sys.stdout.write("''")
        else:
            sys.stdout.write(ch)
        ch = stdin.read(1)
