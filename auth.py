import random

database = {
    2873916105: ["wisdom", "eshiet", "schmulz@guapy.com", "password", 100]
}

def init():

    print("Welcome to bankPHP")


    have_account = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if(have_account == 1):
        login()
    elif(have_account == 2):
        print(register())
    else:
        print("You have selected invalid option")
        init()

def register():

    print("********* Register *********")

    email = input("what is your email address? \n")
    first_name = input("what is your firstName? \n")
    last_name = input("what is your last name? \n")
    password = input("create a password for yourself \n")

    account_number = generating_account_number()

    database[account_number] = [ first_name, last_name, email, password, 0 ]
    
    print("your account number has been created")
    print("== ====== ======== ====== ===")
    print("your account number is: %d" % account_number)
    print("make sure you keep it safe")
    print("== ====== ======== ====== ===")

    login()

def login():
    print("********** login ***********")

    user_account_number = int(input("what is your account number \n"))
    password = input("what is your password \n")

    for account_number, user_details in database.items():
        if(account_number == user_account_number):
            if(user_details[3] == password):
                bank_operation(user_details)

        else:
            print("invalid login details")
            login()
 

def bank_operation(user):

    print("Welcome %s %s" % (user[0], user[1]))

    selected_option = int(input("What will you like to do? (1) deposit (2) withdrawal (3) check_balance (4) logout (5) exit \n"))

    if selected_option  == 1:
        deposit_operation(user)
    elif selected_option == 2:
        withdrawal_operation(user)
    elif selected_option == 3:
        check_account_balance(user)
    elif selected_option == 4:
        logout()
    elif selected_option == 5:
        exit()    
    else:
        print("Invalid option selected, try again!")
        bank_operation(user)

def deposit_operation(user):
    amount = int(input("How much do you want to deposit? \n"))
    user[4] += amount
    print("transaction successful, your balance is %d" % user[4])
    new_operation(user)

def withdrawal_operation(user):
    amount = int(input("How much do you want to withdraw? \n"))
    if user[4] < amount:
        print("transation fail due to Insufficient funds")
    else:
        user[4] -= amount
        print("withdrawal successful!")
        new_operation(user) 

def check_account_balance(user):
    print(user[4])
    new_operation(user)    

def logout():
    return login()

def exit():
    return init()    

def new_operation(user):
    new_transaction = int(input("will you like to make a new transaction? (1) Yes (2) No \n"))
    if new_transaction == 1:
        bank_operation(user)
    elif new_transaction == 2:
        logout()    

def generating_account_number():
    return random.randrange(1111111111, 9999999999)

init()