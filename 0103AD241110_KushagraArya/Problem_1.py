# create a class for AmazonPayWallet 
# instance member :
# ( publice -- owner ....... private member - __value )
# instance methods:
# getter methods (@property):balance():should return balance amount add_money(amt): should add the amount on to the return balance amount
# add_money(amt):should add the amount on ot the remaining the balance and pay(amt):will deduct the amount from the balance or raise a valueerror
class AmazonPayWallet:
    def __init__(self, owner, value):
        self.owner = owner
        self.__value = value

    @property
    def balance(self):
        return self.__value

    def add_money(self, amt):
        self.__value += amt

    def pay(self, amt):
        if amt > self.__value:
            raise ValueError("Insufficient balance")
        self.__value -= amt


# Creating an object
wallet = AmazonPayWallet("Rahul", 500)

print(wallet.owner)
print(wallet.balance)

wallet.add_money(200)
print(wallet.balance)

wallet.pay(300)
print(wallet.balance)
