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
    print('\n=== Contact List (CLI) ===')
    while True:
        print('\nCommands: add | view | edit | delete | search | quit')
        cmd = input('> ').strip().lower()
        if cmd == 'add':
            name = input('Name: ').strip(); phone = input('Phone: ').strip(); email = input('Email (optional): ').strip()
            contacts[name] = {'phone':phone,'email':email}; save_contacts(contacts); print('Added.')
        elif cmd == 'view':
            for n,info in contacts.items(): print(n, info.get('phone',''), info.get('email',''))
        elif cmd == 'edit':
            name = input('Name to edit: ').strip()
            if name not in contacts: print('No such contact'); continue
            info = contacts[name]
            new_name = input(f"Name [{name}]: ").strip() or name
            phone = input(f"Phone [{info.get('phone','')}]: ").strip() or info.get('phone','')
            email = input(f"Email [{info.get('email','')}]: ").strip() or info.get('email','')
            # if name changed, remove old key
            if new_name != name:
                contacts.pop(name)
            contacts[new_name] = {'phone':phone,'email':email}
            save_contacts(contacts); print('Updated.')
        elif cmd == 'delete':
            name = input('Name to delete: ').strip(); contacts.pop(name,None); save_contacts(contacts); print('Deleted if existed')
        elif cmd == 'search':
            q = input('Search name: ').strip().lower()
            for n,info in contacts.items():
                if q in n.lower(): print(n, info.get('phone',''), info.get('email',''))
        elif cmd == 'quit': break
        else: print('Unknown command.')

if __name__ == '__main__':
    contact_list_cli()
