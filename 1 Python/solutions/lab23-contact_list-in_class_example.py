"""
Lab 23: Contact List
Manage a list of contacts with a CSV file and a CRUDL REPL
"""

def load_csv(path):
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


def export_csv(path, contacts):
    """
    Saves contacts list as csv file
    """
    columns = list(contacts[0].keys())
    output = ','.join(columns)+'\n'
    for i in range(len(contacts)):
        for col in columns:
            output += contacts[i][col]  # add the contact's attributes
            if col != columns[-1]:      # avoid adding an extra comma at the end
                output += ','
        if i < len(contacts)-1:         # avoid adding an extra newline at the end
            output += '\n'

    with open(path, 'w') as file:
        file.write(output)


def create(contacts, contact):
    """
    Adds contact to our contact list
    contact: dictionary of new contact
    """
    pass


def read(contacts, name):
    """
    Prints contact information for contacts[name]
    """
    pass


def update(contacts, name, updates):
    """
    Updates existing contact
    updates : dict of updated key:value pairs
    """
    pass


def delete(contacts, name):
    """
    Deletes contact from contact list
    """
    pass


if __name__ == '__main__':
    contacts = load_csv('google_contacts.csv')

    valid_input = ['create', 'read', 'update', 'delete', 'c', 'r', 'u', 'd', 'done']
    while True:
        while True:
            command = input("What would you like to do: ").strip().lower()
            if command in valid_input:
                break
        if command in ['create', 'c']:
            create_dict = {}
            for key in contacts[0].keys():
                create_dict[key] = input(f"Enter {key}: ")
            contacts.append(create_dict)
        elif command in ['read', 'r']:
            name = input("Name: ")
            found = False
            for contact in contacts:
                if name in contact.values():
                    for key, value in contact.items():
                        print(f'{key}: {value}')
                        found = True
            if not found:
                print(f"{name} not found")
        elif command in ['update', 'u']:
            name = input("Name: ")
            found = False
            for i in range(len(contacts)):
                if name in contacts[i].values():
                    found = True
                    field = input("What field do you want to update: ")
                    if field in contacts[i].keys():
                        contacts[i][field] = input("What do you want to set it as: ")
                    else:
                        print(f'{field} not a valid field')
            if not found:
                print(f"{name} doesn't exist")
        elif command in ['delete', 'd']:
            name = input("Who do you want to delete: ")
            for i in range(len(contacts)):
                if name in contacts[i].values():
                    break
            print(f"Deleted: {contacts.pop(i)}")
        elif command == 'done':
            break


    export_csv('contacts.csv', contacts)

