
class Contact(object):
    attr = ['first_name', 'middle_name', 'last_name', 'phone', 'email', 'address', 'sensitivities', 'shoe_size']

    def __init__(self, *args, **kwargs):
        for contact_dict in args:
            for key in contact_dict:
                if key in self.attr:
                    setattr(self, key, contact_dict[key])
        for key in kwargs:
            if key in self.attr:
                setattr(self, key, kwargs[key])
        for prop in self.attr:
            try:
                self.prop
            except AttributeError:
                self.prop = None

        self.props = self.__dict__

    def __repr__(self):
        return str(self.__dict__)


class ContactList(object):

    def __init__(self, csv=None):
        self.contacts = []
        if csv:
            self.contacts += self.loaded_csv(csv)

    def __repr__(self):
        ret = ''
        for contact in contacts:
            ret += f'{contact}\n'
        return ret

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
            for col in columns:
                output += self.contacts[i][col]  # add the contact's attributes
                if col != columns[-1]:      # avoid adding an extra comma at the end
                    output += ','
            if i < len(self.contacts)-1:         # avoid adding an extra newline at the end
                output += '\n'

        with open(path, 'w') as file:
            file.write(output)

    def load_csv(self, path):
        """
        Returns a list where each item is a dictionary of col:cell pairs within the csv
        """
        loaded_csv = []
        with open(path, 'r') as f:
            contents = f.read().split('\n')     # split csv by lines
        columns = contents[0].split(',')        # first line is column names
        for line in contents[1:]:               # iterate over rows
            row = line.split(',')               # split cells by comma
            row_dict = {}
            for i in range(len(columns)):
                row_dict[columns[i]] = row[i]   # add col[i]:row[i] pair to dict
            loaded_csv.append(row_dict)
        return loaded_csv

    def create(self, contact):
        """
        Adds contact to our contact list
        contact: dictionary of new contact
        """
        self.contacts.append(Contact(contact))

    def read(self, name):
        """
        Return contact information for contacts[name]
        """
        for contact in self.contacts:
            if name in contact.props.values():
                return contact

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
            self.contacts.remove(contact)
        else:
            return f'{name} does not exist'


if __name__ == '__main__':
    contacts = ContactList()
    contacts.create({'first_name':'Dungus', 'middle_name':'Beef', 'last_name':'Bigman', 'sensitivities':'beef', 'shoe_size':'XXXXL'})
    contacts.create({'first_name':'Hugh', 'middle_name':'Mung', 'last_name':'Gus', 'phone':777-777-7777, 'email':'gentlegiant@ups.org', 'sensitivities':'size', 'shoe_size':'secret'})
    contacts.create({'first_name':'Tony', 'last_name':'Balonus', 'sensitivities':'processed beef'})
    print(contacts)
    print(contacts.read('Tony'))
    print(contacts.update('Tony', {'phone':234-567-8999, 'hobbies':['absolutely none']}))
