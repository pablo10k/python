import sys

clients = ['pablo', 'ricardo']


def create_client(client_name):
    #se mete la variable client en la funcion
    global clients
    #si el cliente no esta en la lista de clientes:
    if client_name not in clients:
        clients.append(client_name)
    
    else:
        print('Client already is in the client\'s list ')

def list_clients():
    global clients

    for idx, client in enumerate(clients):
        print('{}: {}'.format(idx, client.capitalize()))


def update_client(client_name, update_client_name):
    global clients

    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = update_client_name

    else:
        print('Client is not in client list')


def delete_client(client_name):
    global clients
    
    if client_name in clients:
        clients.remove(client_name)

    else:
        print('Client is not in the client list')


def search_client(client_name):

    for client in clients:
        if client != client_name:
            continue
        else:
            return True


def _print_welcome():
    print('\nBienvenidos a Platzi Ventas')
    print('+' * 27)
    print('What to do doing today?')
    print('[C]reate Client')
    print('[L]ist clients')
    print('[U]pdate client')
    print('[S]earch Client')
    print('[D]elete Client\n')
    

def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name? ')
        
        if client_name.lower() == 'exit':
            client_name = None
            break
    
    if not client_name:
        sys.exit()

    return client_name


if __name__ == "__main__":
    _print_welcome()

    command = input()
    if command.upper() == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    
    elif command.upper() == 'L':
        list_clients()

    elif command.upper() == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()

    elif command.upper() == 'U':
        client_name = _get_client_name()
        update_client_name = input('What is the updated client name? ')
        update_client(client_name, update_client_name)
        list_clients()

    elif command.upper() == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print('The Client is in the client\'s list')
        
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))
   
    else:
        print('Invalid command')
