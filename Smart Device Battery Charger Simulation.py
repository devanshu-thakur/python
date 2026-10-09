a=int(input("Enter current battery percentage (0-99): "))
import time
t=a+5
x=a+10
while True:
    if 80>a>=0 and x<=89:
        time.sleep(2)
        print(f"Charging... {x}%")
        x+=10
    elif 100>=x>=80 and t<=100:
        time.sleep(2)
        print(f"Charging... {x-5}%")
        x+=5
        if x>100:
            time.sleep(2)
            print("Battery Full! Disconnecting charger. 🔋")
            break
        elif t>=100:
            time.sleep(2)
            print("Battery Full! 100% Disconnecting charger. 🔋")
            break
