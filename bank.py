import json
import string
import random
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []

    def __init__(self):
        if Path(self.database).exists():
            with open(self.database) as f:
                self.data = json.load(f)
        else:
            self.data = []
    
    def __update(self):
        with open(self.database, "w") as f:
            json.dump(self.data, f, indent=4)
    
    def __accountgenerate(self):
        return "".join(random.choices(string.digits, k=6))
    
    def Createaccount(self, name, age, email, pin):
        pin = str(pin) 

        if age < 18 or len(pin) != 4 or not pin.isdigit():
            return "Invalid details"

        user = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo": self.__accountgenerate(),
            "balance": 0
        }

        self.data.append(user)
        self.__update()
        return user["accountNo"]
    
    def depositmoney(self, acnum, pin, amount):
        for user in self.data:
            if user['accountNo'] == acnum and user["pin"] == pin:
                if amount <= 0 or amount > 10000:
                    return "Invelid Amount"
                user['balance'] += amount
                self.__update()
                return "Amount Deposited..."
            
        return "Account Not Found"
    
    def withdrawmoney(self, acnum, pin, amount):
        for user in self.data:
            if user["accountNo"] == acnum and user["pin"] == pin:
                if amount <= 0:
                    return "Invalid amount"
                if user['balance'] < amount:
                    return "Insufficient balance"
                user["balance"] -= amount
                self.__update()
                return "Amount withdrawn..."
        return "Account Not Found"
    
    def showdetails(self, acnum, pin):
        for user in self.data:
            if user["accountNo"] == acnum and user["pin"] == pin:
                return user
        return None

    def update_account(self, acnum, pin, name, email, new_pin):
        for user in self.data:
            if user["accountNo"] == acnum and user["pin"] == pin:

                if name:
                    user["name"] = name
                if email:
                    user["email"] = email
                if new_pin:
                    if len(new_pin) == 4 and new_pin.isdigit():
                        user["pin"] = new_pin
                    else:
                        return "Invelid PIN"
                self.__update()
                return "Account updated successfully"
        return "Account Not Found"
    
    def delete_account(self, acnum, pin):
        for user in self.data:
            if user["accountNo"] == acnum and user["pin"] == pin:
                self.data.remove(user)
                self.__update()
                return "Account Deleted..."
        return "Account Not Found"
    
    
