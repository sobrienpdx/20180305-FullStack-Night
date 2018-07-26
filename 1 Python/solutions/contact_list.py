
class Contact(object):
    """ Contact class that behaves like a dictionary for the attributes in self.attr
    """
    # Contact fields
    attr = ['first_name', 'middle_name', 'last_name', 'phone', 'email', 'address', 'sensitivities', 'shoe_size']

    def __init__(self, *args, **kwargs):
        """ Init takes optional args and kwargs where type(args) is dict. Only args and kwargs with keys in self.attr are evaluated
        """
        # Add each item as Contact attribute if its key is in attr
        for contact_dict in args:
            if type(contact_dict) is dict:
                for key in contact_dict:
                    if key in self.attr:
                        setattr(self, key, contact_dict[key])
        for key in kwargs:
            if key in self.attr:
                setattr(self, key, kwargs[key])
        self.props = self.__dict__

    def __repr__(self):
        """ Return string of self.props
        """
        output = ''
        for field in self.props:
            if field in self.attr:
                output += f"{field}: {self.props[field]}\n"
        return output

    def update(self, updates):
        self.props.update(updates)


class ContactList(object):
    # Contact fields
    attr = ['first_name', 'middle_name', 'last_name', 'phone', 'email', 'address', 'sensitivities', 'shoe_size']

    def __init__(self, csv=None):
        if csv:
            self.contacts = self.loaded_csv(csv)
        else:
            self.contacts = {}

    def __repr__(self):
        return '\n'.join(self.contacts)

    def __len__(self):
        return len(self.contacts)

    def __getitem__(self, position):
        return self.contacts[position]

    def export_csv(self, path):
        """
        Saves contacts list as csv file
        """
        columns = list(self.contacts[0].keys())
        output = ','.join(columns)+'\n'
        for i in range(len(self.contacts)):
            output += ','.join(self.contacts[i].values()) + '\n'
            # # The above is equivalent to the following code:
            # for col in columns:
            #     output += self.contacts[i][col]  # add the contact's attributes
            #     if col != columns[-1]:      # avoid adding an extra comma at the end
            #         output += ','
            # if i < len(self.contacts)-1:         # avoid adding an extra newline at the end
            #     output += '\n'

        with open(path, 'w') as file:
            file.write(output)

    def load_csv(self, path):
        """
        Returns a list where each item is a dictionary of col:cell pairs within the csv
        """
        loaded_csv = {}
        with open(path, 'r') as f:
            contents = f.read().split('\n')     # split csv by lines
        columns = contents[0].split(',')        # first line is column names
        for line in contents[1:]:               # iterate over rows
            row = line.split(',')               # split cells by comma
            loaded_csv.append(dict(zip(columns, row)))
            # # The following lines are equivalent to the line above
            # row_dict = {}
            # for i in range(len(columns)):
            #     row_dict[columns[i]] = row[i]   # add col[i]:row[i] pair to dict
            # loaded_csv.append(row_dict)
        return loaded_csv

    def create(self, contact):
        """
        Adds contact to our contact list
        contact: dictionary of new contact
        """
        try:
            self.contacts[contact['first_name'].lower()] = contact
        except KeyError:
            pass            

    def read(self, name):
        """
        Return contact information for contacts[name]
        """
        try:
            return self.contacts[name]
        except KeyError:
            return f"{name} does not exist"

    def update(self, name, updates):
        """
        Updates existing contact
        updates : dict of updated key:value pairs
        """
        contact = self.read(name)
        if contact:
            contact.update(updates)
            return contact
        else:
            return f'{name} does not exist'

    def delete(self, name):
        """
        Deletes contact from contact list
        """
        contact = self.read(name)
        if contact:
            del self.contacts[contact]
        else:
            return f'{name} does not exist'


if __name__ == '__main__':

    # contacts = ContactList()
    # contacts.create({'first_name':'Dungus', 'middle_name':'Beef', 'last_name':'Bigman', 'sensitivities':'beef', 'shoe_size':'XXXXL'})
    # contacts.create({'first_name':'Hugh', 'middle_name':'Mung', 'last_name':'Gus', 'phone':777-777-7777, 'email':'gentlegiant@ups.org', 'sensitivities':'size', 'shoe_size':'secret'})
    # contacts.create({'first_name':'Tony', 'last_name':'Balonus', 'sensitivities':'processed beef'})
    # print(contacts)
    # print(contacts.read('Tony'))
    # print(contacts.update('Tony', {'phone':234-567-8999, 'hobbies':['absolutely none']}))

    # REPL
    help_msg = ('-'*48 +
    '''\nWelcome to your contact list. Enter a command:
    (L)oad to load contacts from csv file
    (S)ave to save contact list to csv file
    (P)rint contact list
    (C)reate contact
    (R)ead contact
    (U)pdate contact
    (D)elete contact
    E(x)it\n''' + '-'*48)
    
    # Welcome screen
    print(help_msg)

    while True:
        commands = {'l', 'load', 's', 'save', 'p', 'print', 'c', 'r', 'u', 'd', 'create', 'read', 'update', 'delete', 'h', 'help', 'x', 'exit'}
        contacts = ContactList()
        
        # Input validation for commands
        while True:
            cmd = input("Please enter a command: ").strip().lower()
            if cmd in commands:
                break

        if cmd.startswith('p'):
            print(contacts)         

        elif cmd.startswith('c'):
            print("Creating new contact\n" + '-'*48)
            contact = {}
            for field in contacts.attr:
                value = input(f"Enter your contact's {field}: ").strip()
                contact[field] = value
            print(contact)
            contacts.create(contact)
            print('-'*48 + f"\nCreated {contact['first_name']}'s contact\n" + '-'*48)

        elif cmd in ['r', 'read', 'u', 'update', 'd', 'delete']:
            query = input("Enter contact name: ").strip().lower()
            
            if cmd.startswith('r'):
                print("Reading contact\n" + '-'*48)
                print(contacts.read(query) + '-'*48)
            
            elif cmd.startswith('u'):
                print("Updating contact\n" + '-'*48)
                contact = contacts.read(query)
                print(contact + '-'*48) 
                if type(contact) is Contact:
                    for field in contacts.attr:
                        value = input(f"Enter your contact's {field} or leave empty for no change: ").strip()
                        if value:
                            contact[field] = value
                    contacts.update(query, contact)                    
                print('-'*48 + f"\nUpdated {contact['first_name']}'s contact\n" + '-'*48)
            
            elif cmd.startswith('d'):
                print("Deleting contact")
                not_found = contacts.delete(query)
                if not_found:
                    print(not_found + '-'*48)
                else:
                    print(f"\nDeleted {contact['first_name']}'s contact\n" + '-'*48)

        elif cmd.startswith('h'):
            print(help_msg)

        elif cmd in ['x', 'exit']:
            break


