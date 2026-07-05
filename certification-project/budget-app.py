class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount,"description": description})
            return True 
        return False 

    def get_balance(self):
        total = 0
        for entry in self.ledger:
            total += entry["amount"]
        return total 


    def transfer(self, amount, destination):
        if self.withdraw(amount, description=f"Transfer to {destination.name}"):
            destination.deposit(amount,f"Transfer from {self.name}")
            return True 
        return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True
    
    def __str__(self):
        title = self.name.center(30, "*")
        lines = [title]

        for entry in self.ledger:
            desc = entry["description"][:23]
            amt = f"{entry['amount']:.2f}"
            lines.append(desc.ljust(23) + amt.rjust(7))

        lines.append(f"Total: {self.get_balance():.2f}")
        return "\n".join(lines)

def create_spend_chart(categories):
    pass