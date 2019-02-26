"""
Lab 23: Contact List
Manage a contact list and save to CSV file with a CRUD REPL interface
"""


class ContactList:
    """
    Contact list as dictionary of dictionaries implementation
    """

    def __init__(self, csv=None, props=None):
        """
        initializes ContactList from csv file or props
        :props: list : list of prop names for contact list
        :csv: str : file path of csv
        """
        if csv is None:
            self.props = props
            self.contacts = {}
            self.csv = 'contact_list.csv'
        else:
            self.csv = csv
            self.load()


    def __repr__(self):
        """
        string representation of ContactList obj
        """
        ret = []
        for contact in self.contact_list:
            ret.append(ContactList.pretty_contact(self.contact_list[contact])+'\n')

        return '\n'.join(ret)


    def load(self):
        """
        reads csv file and parses it into a dictionary of dictionaries
        :csv: str : file path of csv
        """
        with open(self.csv) as f:
            lines = f.read().split('\n')

        contact_list = {}
        props = lines[0].split(',')
        for i in range(1, len(lines)):
            row = lines[i].split(',')
            contact = dict(zip(props, row))
            contact_list[contact['name']] = contact

        self.contact_list = contact_list
        self.props = props    


    @staticmethod
    def pretty_contact(contact):
        """
        pretty prints single contact
        """
        contact_str = []
        if type(contact) is dict:
            for k, v in contact.items():
                contact_str.append(f'{k}: {v}')
            return '\n'.join(contact_str)
        else:
            return contact


    def save(self):
        """
        writes contact_list as csv file
        :csv: str : file path of csv
        """
        contacts = [','.join(self.props)]
        for name in self.contact_list:
            contact = self.contact_list[name]
            contacts.append(','.join(contact.values()))

        with open(self.csv, 'w') as f:
            f.write('\n'.join(contacts))

        return f'Saving contacts as {self.csv}...'


    def create(self, contact):
        """
        adds contact to contact_list
        :contact: dict : individual contact information
        """
        if self.contact_list.get(contact['name']):
            return f"Error: {contact['name']} already exists."

        self.contact_list[contact['name']] = contact
        return f"Created contact for {contact['name']}."


    def read(self, name):
        """
        returns contact with matching name
        :name: str : name of contact
        """
        return self.contact_list.get(name, f'Error: {name} does not exist.')


    def update(self, name, updated_info):
        """
        updates contact with matching name with updated_info
        :contact_list: dict : dict of contacts
        :name: str : name of contact
        :updated_info: dict : contact information
        """
        if self.contact_list.get(name):
            self.contact_list[name].update(updated_info)
            return f'Updated contact for {name}'
        return f'Error: {name} does not exist.'


    def delete(self, name):
        """
        deletes contact with matching name
        :contact_list: dict : dict of contacts
        :name: str : name of contact
        """
        if self.contact_list.get(name):
            del self.contact_list[name]
            return f'{name} deleted.'
        return f'Error: {name} does not exist.'



if __name__ == '__main__':
    contacts = ContactList('contact_list.csv')

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
            cmd = input('> ').strip().lower()
            if cmd in valid_inputs:
                valid = True
            else:
                print('Invalid input.')
                print(commands)

        if cmd in ['x', 'exit', 'quit']:
            # save contacts as csv
            print(contacts.save())
            loop = False
            print('Goodbye!')

        elif cmd in ['e', 'list', 'ls']:
            print(contacts)

        elif cmd in ['h', 'help']:
            print(commands)

        elif cmd.startswith('c'):
            contact = {}
            for prop in contacts.props:
                contact[prop] = input(f'{prop}: ')
            print(contacts.create(contact))

        else:
            name = input('name: ')
            print('-'*60)

            if cmd.startswith('r'):
                contact = contacts.read(name)
                print(ContactList.pretty_contact(contact))

            elif cmd.startswith('u'):
                contact = contacts.read(name)
                if type(contact) is dict:
                    contact = {}
                    for prop in contacts.props:
                        val = input(f'{prop}: ')
                        if val:
                            contact[prop] = val
                    print(contacts.update(name, contact))
                else:
                    print(contact)

            elif cmd.startswith('d'):
                print(contacts.delete(name))