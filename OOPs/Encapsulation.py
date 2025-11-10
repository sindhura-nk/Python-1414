# Combine data and methods together into a single unit. 

'''
We need to use encaspsulation in keeping the customer data safe at XYZ bank.
Hard coding customer data for better understanding of scenario
'''

# protected access: subclasses can access methods and data
customer_data = {
    98787889988:80000,
    87666754665:2000,
    90898767674:15000
}
class XYZ_Bank_login:
    def __init__(self,account_number):
        self._account_number = account_number
    
    def _get_balance(self):
        if self._account_number in customer_data.keys():
            self._balance = customer_data.get(self._account_number)
            if self._balance>1000:
                print(f'Your balance is {self._balance}')
                return True
            else:
                print(f'Insufficient Balance. Minimum balance is 1000')
                return False
        else:
            print(f'Incorrect Account details. Re-enter account number')

class Dedcut_bal(XYZ_Bank_login):
    def __init__(self, account_number,amount):
        super().__init__(account_number)
        self._amount = amount
    def _deduct(self):
        if super()._get_balance():
            if self._amount<self._balance:
                self._balance -=self._amount
                print(f'Amount deduction successful. New balance is {self._balance}')
            else:
                print(f'Insufficient Balance.')


# u1 = XYZ_Bank_login(98787889988)
# u1._get_balance()
u2 = Dedcut_bal(87666754665,800)
u2._deduct()

# private : totally hidden
#hardcoding userid and passwrd
userid = 40132908
passwrd = 'THyuG@223400@mnM'
class user_login:
    def __init__(self,account_number,uid,pwd):
        self._account_number = account_number
        self._uid = uid
        self._pwd = pwd
    
    # def __check_authorization(self):
    #     if (self.__uid == userid) and (self.__pwd == passwrd):
    #         return True
    #     else:
    #         return False


    # to save the important data in private mode
    def __store_data(self):
        self.__userid = 40132908
        self.__passwrd = 'THyuG@223400@mnM'
    def _check_authorization(self):
        if (self._uid == userid) and (self._pwd == passwrd):
            return True
        else:
            return False
u3 = user_login(80888566568,234234234,'THyuG@223400@mnM')
# u3.__check_authorization()
# u3.__store_login_data()
# u3._uid
u3._check_authorization()
