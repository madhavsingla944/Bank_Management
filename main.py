'''
Goals-
create user
view details
deposit money
withdraw money
update user
delete user
'''
import json
import string
import random
from pathlib import Path


class Bank:

    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("no such file exist ")
    except Exception as err:
        print(f"an exception occured as {err}")
    
    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k = 3)
        num = random.choices(string.digits,k= 3)
        spchar = random.choices("!@#$%^&*",k = 1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)

    def CreateAccount(self):
        info = {
            "name" : input("Enter your name -> "),
            "age"  : int(input("Enter your age -> ")),
            "email": input("Enter your email id -> "),
            "pin"  : int(input("Enter your 4 digit pin -> ")),
            "account_no" : Bank.__accountgenerate(),
            "balance" : 0
        }
        if(info["age"] >= 18 and len(str(info["pin"]))  == 4):
            print("Bank Account created successfully!")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please note your account number carefully")
            Bank.data.append(info)
            Bank.__update()
        else:
            print("Can not create Bank Account!")



    def DepositMoney(self):
        acc_no = input("Enter your account no. ")
        pin = int(input("Enter your pin "))

        userdata = [i for i in Bank.data if i["account_no"] == acc_no and i["pin"] == pin]

        if userdata == False:
            print("No user Found")

        else:
            amount = int(input("Enter the amount to be deposited "))
            if amount < 10001 and amount > 0 :
                userdata[0]['balance'] += amount
                Bank.__update()
                print("Amount deposited successfully ")
            else:
                print("Amount must be between 0 and 10k")
    


    def WithdrawMoney(self):
        acc_no = input("Enter your account no. ")
        pin = int(input("Enter your pin "))

        userdata = [i for i in Bank.data if i["account_no"] == acc_no and i["pin"] == pin]

        if userdata == False:
            print("No user Found")

        else:
            amount = int(input("Enter the amount to withdraw "))
            if (userdata[0]["balance"] - amount > 0) :
                userdata[0]['balance'] -= amount
                Bank.__update()
                print("Amount withdrawn successfully ")
            else:
                print("Insufficient Balance")



    def ViewAccount(self):
        acc_no = input("Enter your account no. ")
        pin = int(input("Enter your pin "))

        userdata = [i for i in Bank.data if i["account_no"] == acc_no and i["pin"] == pin]
        # print(userdata[0])
        if userdata == False:
            print("No user found!!")

        else:
            for i in userdata[0]:
                if i == "pin":
                    res = input(("Do you want to display your pin [y/N] "))
                    if res == "y":
                        print(f"{i} : {userdata[0][i]}")
                    else:
                        print("Pin : ****")
                else:
                    print(f"{i} : {userdata[0][i]}")



    def UpdateAccount(self):
        acc_no = input("Enter your account no. ")
        pin = int(input("Enter your pin "))

        userdata = [i for i in Bank.data if i["account_no"] == acc_no and i["pin"] == pin]

        if userdata == False:
            print("No user found!!")

        else:
            print("you cannot change the age, account number, balance")
            print("Fill the details for change or leave it empty if no change")

            print("Enter 1 to change name ")
            print("Enter 2 to change email ")
            print("Enter 3 to change pin ")

            ch = int(input("Enter your response -> "))
            if ch == 1:
                new_name = input("Enter new name ")
                userdata[0]["name"] = new_name
            elif ch == 2:
                new_email = input("Enter new email ")
                userdata[0]["email"] = new_email
            else:
                new_pin = int(input("Enter your new pin "))
                if len(str(new_pin)) == 4:
                    userdata[0]["pin"] = new_pin
                else:
                    print("print valid pin!")

            Bank.__update()
            print("details updated successfully")



    def DeleteAccount(self):
        acc_no = input("Enter your account no. ")
        pin = int(input("Enter your pin "))

        userdata = [i for i in Bank.data if i["account_no"] == acc_no and i["pin"] == pin]

        if userdata == False:
            print("No user found!!")

        else:
            ch = input("Do you really want to delete the account? [y/N] ")

            if ch == "N":
                print("bypassed")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                Bank.__update()
                print("Bank account deleted successfully!")



print("press 1 for creating an account")
print("press 2 for Deposititing the money in the bank ")
print("press 3 for withdrawing the money ")
print("press 4 for details ")
print("press 5 for updating the details")
print("press 6 for deleting your account")


check = int(input("Tell your response -> "))

user = Bank()

if check == 1:
    user.CreateAccount()

if check == 2:
    user.DepositMoney()

if check == 3:
    user.WithdrawMoney()

if check == 4:
    user.ViewAccount()

if check == 5:
    user.UpdateAccount()

if check == 6:
    user.DeleteAccount()