
#imp: Locking a device after 3 wrong password attempts and waiting for 15 seconds before trying again.
c=0
for c in range(4444):
    password="zxmp123"
    i=0
    for i in range(3):
        a=input('Enter Password: ')
        if a==password:
           print("Your Device is Unlocked.😊")
           break
        else:
            print('Wrong Password. Try Again!')
        i+=1
    if a!=password:
        import time
        second=15
        while second>0:
            print(f'Please wait for {second} seconds and then try again.')
            time.sleep(1)
            second-=1
    if a==password:
        break
    c+=1
