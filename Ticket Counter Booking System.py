tickets_left = 10
while True:
    a=int(input('Enter the Number of Tickets: '))
    if 0<a<=tickets_left:
        print(f'collect {a} tickets')
    elif tickets_left==0:
        print("All tickets sold out!")
        break
    else:
        print('Enter a valid number!')
        tickets_left = 10
        while True:
            a=int(input('Enter the Number of Tickets: '))
            if 0<a<=tickets_left:
                print(f'collect {a} tickets')
            elif tickets_left==0:
                print("All tickets sold out!")
                break
    tickets_left-=a
