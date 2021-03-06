# Each contact will be rendered as a dictionary
# Contacts should include first name, last name, full name, company, phone number, e-mail address
# Contacts can be organised in a dictionary (i.e. dictionary of dictionaries) - each key of the outer dictionary will be the name of the contact
# Add contacts: Go through a list of contact details which is supplied by the user
# Delete contacts: Search the list for 'name' keys with a particular value and delete
# Search contacts: Same functionality as for deletion
# Sort contacts: Sort the keys in the dictionary
# How can the contacts list be saved for later (i.e. to avoid having to add them all again?)

# Take a case-insensitive string - use this to search the contacts database
# e.g. 'proquest' - search anything where this is mentioned in company or e-mail address
# Enable functionality to display a specific contact
# List first name, last name, e-mail address


def menu_of_options():
    print(
        """
        ===== MENU =====
        1 - Print the menu
        2 - Print the contacts list
        3 - Add a contact
        4 - Edit a contact by name
        5 - Delete a contact by name
        6 - Save the file
        7 - Sort the contacts
        8 - Search contacts
        9 - Print a contact by name
        0 - Exit
        """)


def add_a_contact(contacts):
    first_name = input("Enter the contact's first name: ")
    last_name = input("Enter the contact's last name: ")
    company = input("Enter the name of the company the contact works for: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's e-mail address: ")
    contacts.append({
        'first_name' : first_name,
        'last_name' : last_name,
        'full_name' : last_name + ', ' + first_name,
        'company' : company,
        'phone' : phone,
        'e-mail' : email
        })
    save_the_contacts(contacts)
    return contacts


def delete_contact(contacts):
    to_edit = input(
            """Enter the name of a contact
            in the form last name, first_name: """).strip()

    contact_to_delete = filter_contact(contacts, 'full_name', to_edit)[0]
    contacts.remove(contact_to_delete)
    save_the_contacts(contacts)

def edit_contact(contacts):
    to_edit = input(
            """Enter the name of a contact
            in the form last name, first_name: """).strip()

    contact_to_edit = filter_contact(contacts, 'full_name', to_edit)[0]


    while True:
        selection = input(
        """
        Which contact field do you want to edit?
        Select from:
        1 - First Name
        2 - Last Name
        3 - Company
        4 - Phone
        5 - E-mail
        : """
        )

        if selection == '1':
            field_to_edit = "first_name"
            break
        elif selection == '2':
            field_to_edit = "last_name"
            break
        elif selection == '3':
            field_to_edit = "company"
            break
        elif selection == '4':
            field_to_edit = "phone"
            break
        elif selection == '5':
            field_to_edit = "e-mail"
            break
        else:
            "Please enter a number from the menu."


    new_value = input("Type replacement text for this field: ")
    contact_to_edit[field_to_edit] = new_value
    if field_to_edit in ['first_name', 'last_name']:
        contact_to_edit['full_name'] = contact_to_edit['last_name'] + ', ' + contact_to_edit['first_name']
    save_the_contacts(contacts)
    return contacts


def filter_contact(contacts, field, value):
    return [contact for contact in contacts if contact[field] == value]


def save_the_contacts(contacts):
    with open('contacts.txt', 'wt') as output_file:
        for contact in contacts:
            for key, value in contact.items():
                if key != 'e-mail':
                    output_file.write(f'{key}:{value}|')
                else:
                    output_file.write(f'{key}:{value}')
            output_file.write('\n')


def search_contacts(contacts):
    search_term = input("Enter text to search for in contacts: ")
    search_term_found = False
    for contact in contacts:
        for key, value in contact.items():
            if value.casefold() in search_term.casefold():
                print(f"\nValue {search_term} found in contact for {contact['full_name']}")
                search_term_found = True
                break
    if not search_term_found:
        print(f"No value {search_term} in contacts database.")


def print_contact_by_name(contacts):
    to_find = input(
            """Enter the name of a contact
            in the form last name, first_name: """).strip()
    contact_to_display = filter_contact(contacts, 'full_name', to_find)[0]
    print(
        f"""
        First Name: {contact_to_display['first_name']}
        Last Name:  {contact_to_display['last_name']}
        E-mail: {contact_to_display['e-mail']}
        """)


with open('contacts.txt', 'rt') as input_file:
    contacts = []
    for contact in [line.strip() for line in input_file]:
        contacts.append(dict([tuple(i.split(':')) for i in contact.split('|')]))


while True:
    # Where user is required to type words, don't mix case
    # use numbers for basic options
    menu_of_options()
    selection = input("Enter a number from the menu: ")

    if selection == '1':
        menu_of_options()
    elif selection == '2':
        print(contacts)
    elif selection == '3':
        add_a_contact(contacts)
    elif selection == '4':
        edit_contact(contacts)
    elif selection == '5':
        delete_contact(contacts)
    elif selection == '6':
        save_the_contacts(contacts)
    elif selection == '7':
        contacts.sort(key = lambda i: i['last_name'])
    elif selection == '8':
        search_contacts(contacts)
    elif selection == '9':
        print_contact_by_name(contacts)
    elif selection == '0':
        break
    else:
        "Please enter a number from the menu."
