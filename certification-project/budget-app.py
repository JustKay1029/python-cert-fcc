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


#used ai / comet browser's assistant to write this portion becuase the OOPs concept is made clear above
#below it's just "string - art" about spacing and writing which doesn't really contribute to learning
def create_spend_chart(categories):
    lines = ["Percentage spent by category"]
    spent_amounts = []
    for category in categories:
        spent = 0
        for entry in category.ledger:
            if entry["amount"] < 0:
                spent += -entry["amount"]
        spent_amounts.append(spent)
    
    total_spent = sum(spent_amounts)

    percentages = []
    for spent in spent_amounts:
        percent = (spent / total_spent) * 100
        percentages.append(int(percent // 10) * 10)

    for i in range(100, -1, -10):
        line = f"{i:>3}| "
        for percent in percentages:
            if percent >= i:
                line += "o  "
            else:
                line += "   "
        lines.append(line)

    lines.append("    " + "-" * (len(categories) * 3 + 1))

    max_len = max(len(category.name) for category in categories)
    for i in range(max_len):
        line = "     "
        for category in categories:
            if i < len(category.name):
                line += category.name[i] + "  "
            else:
                line += "   "
        lines.append(line)

    return "\n".join(lines)