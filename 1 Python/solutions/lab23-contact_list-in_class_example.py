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
    export_csv('contacts.csv', contacts)