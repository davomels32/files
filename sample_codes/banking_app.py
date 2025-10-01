import json, os

DATA_FILE = "bank_accounts.json"

def load_accounts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE,"r") as f:
            return json.load(f)
    return {}

def save_accounts(accounts):
    with open(DATA_FILE,"w") as f:
        json.dump(accounts,f,indent=4)

def banking_cli():
    print("\n=== Banking App (CLI) ===")
    accounts = load_accounts()
    while True:
        print("\nCommands: create | login | quit")
        cmd = input("> ").strip().lower()
        if cmd == "create":
            user = input("Username: ").strip()
            if user in accounts:
                print("User exists.")
                continue
            pin = input("4-digit PIN: ").strip()
            accounts[user] = {"pin":pin,"balance":0.0}
            save_accounts(accounts); print("Account created.")
        elif cmd == "login":
            user = input("Username: ").strip()
            pin = input("PIN: ").strip()
            if user not in accounts or accounts[user]["pin"] != pin:
                print("Invalid credentials.")
                continue
            print(f"Welcome {user}")
            while True:
                print("Commands: deposit | withdraw | balance | logout")
                c = input("-> ").strip().lower()
                if c == "deposit":
                    amt = float(input("Amount: "))
                    accounts[user]["balance"] += amt; save_accounts(accounts)
                    print(f"Balance: {accounts[user]['balance']:.2f}")
                elif c == "withdraw":
                    amt = float(input("Amount: "))
                    if amt > accounts[user]["balance"]:
                        print("Insufficient funds.")
                    else:
                        accounts[user]["balance"] -= amt; save_accounts(accounts)
                        print(f"Balance: {accounts[user]['balance']:.2f}")
                elif c == "balance":
                    print(f"Balance: {accounts[user]['balance']:.2f}")
                elif c == "logout":
                    break
                else:
                    print("Unknown command.")
        elif cmd == "quit":
            break
        else:
            print("Unknown command.")

if __name__ == '__main__':
    banking_cli()
