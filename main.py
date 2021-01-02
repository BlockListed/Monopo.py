import json

class bank:
    def __init__(self):
        print("Initiated")
        self.MonoBank = dict({})
    
    def Command(self):
        # Do commandparsing and other shit
        cmd = input("MonoShell $ ")
        cmdparts = cmd.split(" ")

        # This is really ineffecient, but this is a simple program, also if I do it better it's gonna be a lot more work!
        if cmdparts[0] == "add":
            print(self.add(cmdparts[1], int(cmdparts[2])))
        elif cmdparts[0] == "subtract":
            print(self.subtract(cmdparts[1], int(cmdparts[2])))
        elif cmdparts[0] == "transfer":
            print(self.transfer(cmdparts[1], cmdparts[2], int(cmdparts[3])))
        elif cmdparts[0] == "new":
            print(self.new(cmdparts[1]))
        elif cmdparts[0] == "delete":
            print(self.delete(cmdparts[1]))
        elif cmdparts[0] == "save":
            print(self.save(cmdparts[1]))
        elif cmdparts[0] == "load":
            print(self.load(cmdparts[1]))
        elif cmdparts[0] == "list":
            print(self.ls())
        elif cmdparts[0] == "help":
            print(self.help())

    def add(self, account, amount):
        if self.MonoBank.get(account, "noacct") != "noacct":
            self.MonoBank.update({account: (self.MonoBank.get(account) + amount)})
            return f"Added {amount} to {account} (New total {(self.MonoBank.get(account))})!"
        else:
            return f"Account {account} not found!"

    def subtract(self, account, amount):
        if self.MonoBank.get(account, "noacct") != "noacct":
            self.MonoBank.update({account: (self.MonoBank.get(account) + amount)})
            return f"Subtracted {amount} from {account} (New total {(self.MonoBank.get(account))})!"
        else:
            return f"Account {account} not found!"

    def transfer(self, src, target, amount):
        if self.MonoBank.get(src, "noacct") != "noacct" and self.MonoBank.get(target, "noacct") != "noacct":
            srctotal = self.MonoBank.get(src)
            targettotal = self.MonoBank.get(target)
            newsrctotal = srctotal - int(amount)
            newtargettotal = targettotal + int(amount)
            self.MonoBank.update({src: newsrctotal, target: newtargettotal})
            return f"{amount} transfered from {src} to {target} (New totals: {src}: {newsrctotal}, {target}: {newtargettotal})!"
        else:
            return f"Account {src} or {target} not found!"

    def new(self, account):
        if self.MonoBank.get(account, "noacct") == "noacct":
            self.MonoBank.update({str(account): 0})
            return f"Added account {account}!"

        else:
            return f"Account {account} already exists!"

    def delete(self, account):
        if self.MonoBank.get(account, "noacct") != "noacct":
            self.MonoBank.pop(account, None)
            return f"Account {account} deleted!"

        else:
            return f"Account {account} doesn't exist!"

    def save(self, file):
        with open(f"{file}.json", "w") as f:
            f.write(json.dumps(self.MonoBank))
        return f'Saved the database to file "{file}.json"!'

    def load(self, file):
        with open(f"{file}.json", "r") as f:
            self.MonoBank = json.load(f)
        return f'Loaded the database from file "{file}.json"!'

    def ls(self):
        return self.MonoBank

    def help(self):
        return '''
        Help page:
        new [account] - Create a new account
        delete [account] - Delete a new account
        add [account] [amount] - Add money to an account
        subtract [account] [amount] - Subtract money from an account
        transfer [srcaccount] [targetaccount] [amount] - Transfer money between accounts
        save [file] - Save the database to a file
        load [file] - Load the database from a file
        list - List the database
        help - Show this page'''

def main():
    mono = bank()
    while True:
        mono.Command()

main()