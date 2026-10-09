""" def generate_username(first_name, last_name):
    a=first_name.strip()
    c=a.lower()
    b=last_name.strip()
    d=b.lower()
    print(c[0]+d)
generate_username(input("First name: "),input('Last name: ')) """
""" def total_daily_sales(morning_sales, afternoon_sales):
    a=sum(morning_sales)
    b=sum(afternoon_sales)
    c=a+b
    print(c)
mor=list(map(int,input('Enter morning sales: ').split()))
aft=list(map(int,input('Enter afternoon sales: ').split()))
total_daily_sales(mor,aft) """    



""" def validate_coupon(code):
    a=code.strip()
    b=a.upper()
    if "SAVE" in b or "DISC" in b and a[-1:-3]==int:
        print(True)
    else:
        print(False)
validate_coupon(input('Enter the coupon code: ')) """

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

#High-Score Tracker (Finding the Best)3
""" def get_leaderboard(scores_list):
    a=scores_list.sort(reverse=True)
    
    print(scores_list[0], scores_list[1], scores_list[2])
get_leaderboard(list(map(int,input("Enter scores here: ").split()))) """

#The ATM Cash Withdrawal System (Tracking Variables & Limits)
""" print('---------Welcome to Evan Bank------------')
def withdraw_cash(account_balance, request_amount):
    if request_amount>500:
        print('Transaction Denied: Exceeds daily limit of $500.')
    elif request_amount>account_balance:
        print("Transaction Denied: Insufficient funds.")
    else:
        a=account_balance-request_amount
        print("Transaction Successful! New balance: ",a)
        print(f"Please collect your Cash.\n-----Thank You for using Evan Bank-----")

withdraw_cash(int(input('Enter the account balnce:')), int(input('Enter the Amount to Withdraw:'))) """

""" #The Ticket Counter Booking System (Loops & Deductions)
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
        break
        a=int(input('Enter the Number of Tickets: '))
    tickets_left-=a """