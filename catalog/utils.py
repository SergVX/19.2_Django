import json


def save_contact_data(name, phone, message):
    contact_data = {
        'name': name,
        'phone': phone,
        'message': message
    }

    with open('contact_data.json', 'a') as file:
        json.dump(contact_data, file)
        file.write('\n')