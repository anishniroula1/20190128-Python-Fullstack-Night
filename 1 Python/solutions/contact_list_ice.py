"""
Lab 23: Contact List
Manage a contact list and save to CSV file with a CRUD REPL interface
"""

def load(csv):
    """
    reads csv file and parses it into a dictionary of dictionaries
    :csv: str : file path of csv
    """
    with open(csv) as f:
        lines = f.read().split('\n')
    
    contact_list = {}
    props = lines[0].split(',')
    for i in range(1, len(lines)):
        row = lines[i].split(',')
        contact = dict(zip(props, row))
        contact_list[contact['name']] = contact
    
    return (contact_list, props)


def create(contact_list, contact):
    """
    adds contact to contact_list
    :contact_list: dict : dict of contacts
    :contact: dict : individual contact information
    """
    if type(read(contact_list, contact['name'])) is dict:
        return f"Error: {contact['name']} already exists."

    contact_list[contact['name']] = contact
    return f"Created contact for {contact['name']}."


# def find_contact(contact_list, name):
#     for i in range(contact_list):
#         if contact_list[i]['name'] == name:
#             return i


def read(contact_list, name):
    """
    returns contact with matching name
    :contact_list: dict : dict of contacts
    :name: str : name of contact    
    """
    return contact_list.get(name, f'Error: {name} does not exist.')
    # index = find_contact(contact_list, name)
    # if index:
    #     return contact_list[i]
    # else:
    #     return 'Contact not found'


def update(contact_list, name, updated_info):
    """
    updates contact with matching name with updated_info
    :contact_list: dict : dict of contacts
    :name: str : name of contact
    :updated_info: dict : contact information
    """
    if contact_list.get(name):
        contact_list[name].update(updated_info)
        return f'Updated contact for {name}'
    return f'Error: {name} does not exist.'


def delete(contact_list, name):
    """
    deletes contact with matching name
    :contact_list: dict : dict of contacts
    :name: str : name of contact    
    """
    if contact_list.get(name):
        del contact_list[name]
        return f'{name} deleted.'
    return f'Error: {name} does not exist.'


def list_all(contact_list):
    """
    pretty prints all contacts
    """
    for contact in contact_list:
        for k, v in contact_list[contact].items():
            print(f'{k}: {v}')
        print()


if __name__ == '__main__':
    contacts, props = load('contact_list.csv')
    loop = True
    valid_inputs = ['c', 'r', 'u', 'd', 'e', 'x', 'h']
    commands = """ 
        Commands: 
        (c)reate 
        (r)ead 
        (u)pdate 
        (d)elete
        (e)xpand list
        e(x)it
        (h)elp
    """
    print('Welcome to your contact list')
    print(commands)
    while loop:
        print('-'*60)
        while True:
            cmd = input('> ').strip().lower()
            if cmd in valid_inputs:
                break
            print('Invalid input.')
            print(commands)

        if cmd == 'x':
            loop = False
            print('Goodbye!')

        elif cmd.startswith('c'):
            contact = {}
            for prop in props:
                contact[prop] = input(f'{prop}: ')
            print(create(contacts, contact))

        elif cmd.startswith('r'):
            name = input('Name: ')
            print(read(contacts, name))

        elif cmd.startswith('u'):
            name = input('Name: ')            
            contact = {}
            for prop in props:
                val = input(f'{prop}: ')
                if val:
                    contact[prop] = val
            print(update(contacts, name, contact))

        elif cmd.startswith('d'):
            name = input('Name: ')
            print(delete(contacts, name))

        elif cmd == 'e':
            list_all(contacts)

        else: # cmd == 'h'
            print(commands)



