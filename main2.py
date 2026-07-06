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
            pass  # file will be created on first write
    except Exception as err:
        print(f"an exception occured as {err}")

    @classmethod
    def _Bank__update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(Bank.data, indent=4))

    @classmethod
    def _Bank__accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)

    def CreateAccount(self, name, age, email, pin):
        info = {
            "name": name,
            "age": int(age),
            "email": email,
            "pin": int(pin),
            "account_no": Bank._Bank__accountgenerate(),
            "balance": 0
        }
        if info["age"] >= 18 and len(str(info["pin"])) == 4:
            Bank.data.append(info)
            Bank._Bank__update()
            return True, info
        else:
            return False, "Age must be 18+ and PIN must be exactly 4 digits."

    def DepositMoney(self, acc_no, pin, amount):
        userdata = [i for i in Bank.data if i["account_no"] == acc_no and i["pin"] == int(pin)]
        if not userdata:
            return False, "No user found. Check account number and PIN."
        amount = int(amount)
        if 0 < amount <= 10000:
            userdata[0]['balance'] += amount
            Bank._Bank__update()
            return True, f"Rs.{amount} deposited successfully! New balance: Rs.{userdata[0]['balance']}"
        else:
            return False, "Amount must be between Rs.1 and Rs.10,000."

    def WithdrawMoney(self, acc_no, pin, amount):
        userdata = [i for i in Bank.data if i["account_no"] == acc_no and i["pin"] == int(pin)]
        if not userdata:
            return False, "No user found. Check account number and PIN."
        amount = int(amount)
        if userdata[0]["balance"] - amount >= 0:
            userdata[0]['balance'] -= amount
            Bank._Bank__update()
            return True, f"Rs.{amount} withdrawn successfully! New balance: Rs.{userdata[0]['balance']}"
        else:
            return False, "Insufficient balance."

    def ViewAccount(self, acc_no, pin):
        userdata = [i for i in Bank.data if i["account_no"] == acc_no and i["pin"] == int(pin)]
        if not userdata:
            return False, "No user found. Check account number and PIN."
        return True, userdata[0]

    def UpdateAccount(self, acc_no, pin, field, new_value):
        userdata = [i for i in Bank.data if i["account_no"] == acc_no and i["pin"] == int(pin)]
        if not userdata:
            return False, "No user found. Check account number and PIN."
        if field == "name":
            userdata[0]["name"] = new_value
        elif field == "email":
            userdata[0]["email"] = new_value
        elif field == "pin":
            if len(str(new_value)) == 4:
                userdata[0]["pin"] = int(new_value)
            else:
                return False, "New PIN must be exactly 4 digits."
        Bank._Bank__update()
        return True, "Details updated successfully!"

    def DeleteAccount(self, acc_no, pin):
        userdata = [i for i in Bank.data if i["account_no"] == acc_no and i["pin"] == int(pin)]
        if not userdata:
            return False, "No user found. Check account number and PIN."
        index = Bank.data.index(userdata[0])
        Bank.data.pop(index)
        Bank._Bank__update()
        return True, "Account deleted successfully!"
