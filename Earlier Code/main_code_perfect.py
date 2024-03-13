class BankAccount:

    no_of_cust = 0
    acc_num = 42010

    def __init__(self, name, mobile_no, initial_depo, pin):
        
        self.name                 = name
        self.cust_acc_num         = BankAccount.acc_num
        self.mobile_no            = mobile_no
        self.acc_balance          = initial_depo
        self.pin                  = pin
        
        BankAccount.acc_num       = BankAccount.acc_num + 1
        BankAccount.no_of_cust    = BankAccount.no_of_cust + 1

    def basic_details(self):
        print(f'User: {self.name}\t Account No: {self.cust_acc_num}\t Balance: ₹{self.acc_balance}')

    def deposit(self):
        amount = int(input('Enter the deposit amount: '))
        if amount > 0:
            self.acc_balance      = self.acc_balance + amount
            print(f'Transaction completed. Current Balance: ₹{self.acc_balance}')
        else:
            print('Invalid amount transaction aborted')

    def withdrawl(self):
        amount = int(input('Enter the withdrawl amount: '))
        if amount <= self.acc_balance and amount > 0:
            self.acc_balance      = self.acc_balance - amount
            print(f'Transaction completed. Current Balance: ₹{self.acc_balance}')
        else:
            print('Invalid amount transaction aborted')

    def payment(self, other):
        amount = int(input('Enter the payment amount: '))
        if amount <= self.acc_balance and amount > 0:
            self.acc_balance      = self.acc_balance - amount
            other.acc_balance     = other.acc_balance + amount
            print(f'Transaction completed. Current Balance: ₹{self.acc_balance}')
        else:
            print('Invalid amount transaction aborted')

customer_dict = {}              # use account no. as key and class object(customer account) as value
mobile_acc_link = {}            # use mobile no. as key and store account no. as value, for linking purpose

def new_cust():
    name = input('Enter the name of customer: ')
    if name.isalpha() != True:
        print("Enter valid name in string")
        return
    mobile_no = int(input('Enter the mobile number of customer: '))
    if len(str(mobile_no)) != 10:
        print('Invalid range')
        return
    
    initial_depo = int(input('Enter the initial deposit amount: '))
    
    if initial_depo <= 0:
        print('Invalid Amount')
        return
    pin = int(input('Create PIN: '))
   
  
    customer = BankAccount(name=name, mobile_no=mobile_no, initial_depo=initial_depo, pin=pin)    #OBJ
    customer_dict[customer.cust_acc_num] = customer                 # acct. no. stored as key and oject as value
    mobile_acc_link[customer.mobile_no] = customer.cust_acc_num     # mobile no. linked
    print('New User Created!')
    print(f'Welcome {customer.name} to Corporate Bank. {customer.cust_acc_num} is your account number')

def login():
    account_no = int(input('Enter your Account Number: '))
    account_pin = int(input('Enter your Account PIN: '))
    if account_no in customer_dict.keys() and account_pin == customer_dict[account_no].pin :
        print(f'\n{customer_dict[account_no].name} Logged in')
        customer_dict[account_no].basic_details()
    else:
        print('Account either not exist or the pin is wrong')
        return
    while True:
        user_input1 = input('''Press 1 for deposit:
Press 2 for withdrawl:
Press 3 for money transfer:
Press 4 to log out\n''')
        if user_input1 == '1':
            customer_dict[account_no].deposit()
        elif user_input1 == '2':
            customer_dict[account_no].withdrawl()
        elif user_input1 == '3':
            recipient_account_no = int(input('Enter the account number of the recipient: '))
            if recipient_account_no in customer_dict.keys():
                customer_dict[account_no].payment(customer_dict[recipient_account_no])
            else:
                print('The account number you have entered does not exist.')
            
        elif user_input1 == '4':
            print('Logged Out')
            return
        else:
            print('Invalid input try again')
        print('\n#############################################################\n')
        customer_dict[account_no].basic_details()



while True:
    user_input1 = input('''Press 1 for creating a new customer:
Press 2 for logging in as an existing customer:
Press 3 for displaying number of customers:
Press 4 for exit\n''')

    if user_input1 == '1':
        print('Create user')
        new_cust()
    elif user_input1 == '2':
        login()
    elif user_input1 == '3':
        print('There currently', BankAccount.no_of_cust,'customers in Corporate bank.')
        print("Customer Detail\n")
        
        for account_no, customer in customer_dict.items():
            customer.basic_details()
            
                  
    elif user_input1 == '4':
        print('Exited')
        break
    else:
        print('Invalid input try again')
    print('\n*************************************************************\n')