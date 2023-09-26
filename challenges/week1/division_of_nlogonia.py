k = int(input())
while k != 0:
    xo, yo = map(int, input().split())
    for _ in range(k):
        x, y = map(int, input().split())
        if x == xo or y == yo:
            print('divisa')
        elif x > xo and y > yo:
            print('NE')
        elif x < xo and y > yo:
            print('NO')
        elif x < xo and y < yo:
            print('SO')
        else:
            print('SE')
    k = int(input())
