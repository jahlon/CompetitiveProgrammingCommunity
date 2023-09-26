import sys

def print_balances(balances):
    output = ""
    for name in balances:
        output += f'{name} {balances[name]}' + '\n'
    return output + "\n"


res = ""
with sys.stdin as stdin:
    line = stdin.readline()
    while line != '' and line != '\n':
        n = int(line)
        names = stdin.readline().split()
        balances = {name: 0 for name in names}
        for _ in range(n):
            data = stdin.readline().split()
            giver = data[0]
            amount = int(data[1])
            num_receivers = int(data[2])
            
            if num_receivers > 0:                           
                for name in data[3:]:
                    balances[name] += amount // num_receivers
                
                balances[giver] -= amount
                balances[giver] += amount % num_receivers
        
        res += print_balances(balances)
        line = stdin.readline()
    
    print(res[:-2])
