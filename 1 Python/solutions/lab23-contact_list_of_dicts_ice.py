# contact_list_of_dicts_ice.py
"""
Lab 23: Contact List
Manage a contact list and save to CSV file with a CRUD REPL interface
Contact list as list of dictionaries implementation
"""


def load(csv):
    """
    reads csv file and parses it into a dictionary of dictionaries
    :csv: str : file path of csv
    """
    with open(csv) as f:
        lines = f.read().split('\n')

    contact_list = []
    props = lines[0].split(',')
    for i in range(1, len(lines)):
        row = lines[i].split(',')
        contact = dict(zip(props, row))
        contact_list.append(contact)

    return (contact_list, props)


def save(contact_list, props, csv):
    """
    writes contact_list as csv file
    :contact_list: list : list of contacts
    :csv: str : file path of csv
    """
    contacts = [','.join(props)]
    for contact in contact_list:
        contacts.append(','.join(contact.values()))

    with open(csv, 'w') as f:
        f.write('\n'.join(contacts))

    return f'Saving contacts as {csv}...'


def find_contact(contact_list, name):
    """
    return index of a contact in contact_list with a matching name
    :contact_list: list : list of contacts
    :name: str : name of contact
    """
    for i in range(len(contact_list)):
        contact = contact_list[i]
        if contact['name'] == name:
            return i


def create(contact_list, contact):
    """
    adds contact to contact_list
    :contact_list: list : list of contacts
    :contact: dict : individual contact information
    """
    index = find_contact(contact_list, contact['name'])
    if index is not None:
        return f"Error: {contact['name']} already exists."

    contact_list.append(contact)
    return f"Created contact for {contact['name']}."


def read(contact_list, name):
    """
    returns contact with matching name
    :contact_list: list : list of contacts
    :name: str : name of contact
    """
    index = find_contact(contact_list, name)
    if index is None:
        return f'Error: {name} does not exist.'

    return contact_list[index]


def update(contact_list, name, updated_info):
    """
    updates contact with matching name with updated_info
    :contact_list: list : list of contacts
    :name: str : name of contact
    :updated_info: dict : contact information
    """
    index = find_contact(contact_list, name)
    if index is None:
        return f'Error: {name} does not exist.'
        
    contact_list[index].update(updated_info)
    return f'Updated contact for {name}'


def delete(contact_list, name):
    """
    deletes contact with matching name
    :contact_list: list : list of contacts
    :name: str : name of contact
    """
    index = find_contact(contact_list, name)
    if index is None:
        return f'Error: {name} does not exist.'
        
    contact_list.pop(index)
    return f'{name} deleted.'


def print_contact(contact):
    """
    pretty prints single contact
    """
    if type(contact) is dict:
        for k, v in contact.items():
            print(f'{k}: {v}')
    else:
        print(contact)


def list_all(contact_list):
    """
    pretty prints all contacts
    """
    for contact in contact_list:
        print_contact(contact)
        print()


if __name__ == '__main__':
    contacts, props = load('contact_list.csv')
    loop = True
    valid_inputs = [
        'c', 'create',
        'r', 'read',
        'u', 'update',
        'd', 'delete',
        'e', 'list', 'ls',
        'x', 'exit', 'quit',
        'h', 'help'
    ]
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
        valid = False

        while not valid:
            cmd = input('cmd> ').strip().lower()
            if cmd in valid_inputs:
                valid = True
            else:
                print('Invalid input.')
                print(commands)

        if cmd in ['x', 'exit', 'quit']:
            # save contacts as csv
            print(save(contacts, props, 'contact_list.csv'))
            loop = False
            print('Goodbye!')

        elif cmd in ['e', 'list', 'ls']:
            list_all(contacts)

        elif cmd in ['h', 'help']:
            print(commands)

        elif cmd.startswith('c'):
            contact = {}
            for prop in props:
                contact[prop] = input(f'{prop}: ')
            print(create(contacts, contact))

        else:
            name = input('name: ')

            # if name not in contact_list, prompt user to create one instead
            index = find_contact(contacts, name)
            if index is None:
                print('Error:', name, 'does not exist.')

                if not cmd.startswith('d'):
                    create_instead = input(f'Do you want to create a contact for {name}? ').strip().lower()
                    if create_instead in ['y', 'yes']:
                        contact = {}
                        for prop in props:
                            contact[prop] = input(f'{prop}: ')
                        print(create(contacts, contact))
                continue             

            print('-'*60)

            if cmd.startswith('r'):
                contact = read(contacts, name)
                print_contact(contact)

            elif cmd.startswith('u'):
                contact = {}
                for prop in props:
                    val = input(f'{prop}: ')
                    if val:
                        contact[prop] = val
                print(update(contacts, name, contact))

            elif cmd.startswith('d'):
                confirmation = input('are you sure? ').strip().lower()
                if confirmation in ['y', 'yes']:
                    print(delete(contacts, name))
                else:
                    print('Aborting...')
