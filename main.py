

def main():
    flag = True
    while flag:
        command = input('Write your command: ').lower().strip().split()

        try:
            base_command = command[0]
        except IndexError:
            continue

        handler = handler_command(base_command, command)

        if isinstance(handler, str):
            print(handler)
        
        elif isinstance(handler, bool):
            flag = handler

        else:
            handler


def input_error(func):
    def inner(base_command, command):
        try:
            func(base_command, command)
        except KeyError:
            if base_command == 'change' :
                return 'The name is unknown'
            else:
                return 'The command is not exist'
            
        except ValueError:
            return 'Phone number must consist of numbers'
        
        except IndexError:
            if base_command == 'add' or base_command == 'change' or base_command == 'phone':
                return 'Not given name or phone number'
            else:
                return

        else:
            return func(base_command, command)
    return inner


def hello(command):
    return 'How can I help you?'

def add(command):
    name = command[1]
    phone_num = command[2]

    if not phone_num.isdigit():
        raise ValueError
    else:
        contacts[name] = phone_num

def change(command):
    name = command[1]
    phone_num = command[2]
    if name in contacts:
        contacts[name] = phone_num

def phone(command):
    name = command[1]
    if name in contacts:
        return contacts[name]
    else:
        raise IndexError

def show_all(command):
    all_contacts = ''
    for contact, phone in contacts.items():
        all_contacts += f'Name: {contact:<10} Phone number: {phone}\n'

    return all_contacts

def end_program(command):
    return False


contacts = {}

OPERATIONS = {
    'hello': hello,
    'add': add,
    'change': change,
    'phone': phone,
    'show': show_all,
    'good': end_program, 
    'close': end_program, 
    'exit': end_program, 
    '.': end_program, 
}

@input_error
def handler_command(base_command, command):
    return OPERATIONS[base_command](command)


main()