import json, os

DATA_FILE = 'contacts.json'

def load_contacts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE,'r') as f:
            return json.load(f)
    return {}

def save_contacts(contacts):
    with open(DATA_FILE,'w') as f:
        json.dump(contacts,f,indent=4)

def contact_list_cli():
    contacts = load_contacts()
    print("\n=== Contact List (CLI) ===")
    while True:
        print("Commands: add | view | delete | search | quit")
        cmd = input("> ").strip().lower()
        if cmd == 'add':
            name = input('Name: ').strip(); phone = input('Phone: ').strip()
            contacts[name] = phone; save_contacts(contacts); print('Added.')
        elif cmd == 'view':
            for n,p in contacts.items(): print(n,p)
        elif cmd == 'delete':
            name = input('Name to delete: ').strip(); contacts.pop(name,None); save_contacts(contacts); print('Deleted if existed')
        elif cmd == 'search':
            q = input('Search name: ').strip().lower()
            for n,p in contacts.items():
                if q in n.lower(): print(n,p)
        elif cmd == 'quit':
            break
        else:
            print('Unknown command.')

if __name__ == '__main__':
    contact_list_cli()
