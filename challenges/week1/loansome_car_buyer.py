while True:
    duration, down_pay,  loan, n = map(float, input().split())
    
    if duration < 0:
        break
    
    car_value = loan + down_pay
    payment = loan / duration
    months = 0
    dep_rates = []
    
    i = 0
    while i <= duration:
        if i < n:
            month, dep_rate = map(float, input().split())
        
        if month > i:
            for j in range(int(month - i)):
                dep_rates.append(last_rate)
            i += int(month - i)
        else:
            dep_rates.append(dep_rate)
            i += 1
        
        last_rate = dep_rate
            
    car_value *= (1 - dep_rates[0])
    
    while car_value < loan:
        months += 1
        car_value *= (1 - dep_rates[months])
        loan -= payment
        
    if months == 1:
        print(f'{int(months)} month')
    else:
        print(f'{int(months)} months')
    