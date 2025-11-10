## Hiding the implementation details. Showcase the part that is necessarily for the user to see and know.

from abc import ABC,abstractmethod
'''
example: Bank application. Payment related. Credit card, Debit card, Internet Banking
UPI selection: 
1. Enter the UPI id , 
2. it checks valid or not, 
3. it connects to the Bank server, if the server connection is successful,
4. it checks for the balance, 
5. it deducts the amount
'''
class PaymentProcess(ABC):
    def __init__(self):
        super().__init__()
    @abstractmethod
    def pay(self):
        print(f'Payment Initiated')

# predefine UPI'ids 
upi_ids = ['945655556@hdfc','4555555@ramanICICI','678678678@hdfc']

# server details
server = True

class upi_payment(PaymentProcess):
    def __init__(self,upi_id,amount):
        super().__init__()
        self.upi_id = upi_id
        self.amount=amount
    
    def pay(self):
        self.valid_upi_id()
    
    def valid_upi_id(self):
        if self.upi_id in upi_ids:
            bank_message = self.bank_connectivity()
            if bank_message:
               self.check_balance_deduct()
            else:
               print(f'Server Connectivity Issues')             
        else:
            print(f'Incorrect UPI ID. Please provide it again.')

    def bank_connectivity(self):
        if server:
            print(f'Server Connectivity Succesful')
            return True
        else:
            print(f'Server connectivity Issue. Unsuccessful')
            return False

    def check_balance_deduct(self):
        if self.amount<100000:
            print(f'Amount deducted from balance successfully')
        else:
            print(f'Insufficient balance')

upi1 = upi_payment('945655556@hdfc',150000)
upi1.pay()
