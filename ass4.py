# 4. Class Variables and Class Methods
class Bank:
    bank_name = "Bank of Python"

    @classmethod
    def change_bank_name(cls, name:str):
        cls.bank_name = name 

b1 = Bank()       
print(b1.bank_name)     
b1.change_bank_name("Bank of Java")
print(b1.bank_name)
b2 = Bank()
print(b2.bank_name)
b2.change_bank_name("Bank of C++")
print(b2.bank_name)
b3 = Bank()
print(b3.bank_name)
b3.change_bank_name("Bank of C#")
print(b3.bank_name)