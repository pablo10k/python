# -*- coding: utf-8 -*-

import csv

class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class ContactBook:

    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        #add es un metodo de la clase    (una funcion dentro de una clase se llama metodo)
        #se llama a la clase Contact para seguir estructura del contacto, luego se guarda con el append en linea mas abajo
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()

    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break
    
    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()

    def _not_found(self):
        print('*****************')
        print('NOT FOUND!!')
        print('*****************')

    def show_all(self):
        #por cada contacto(var contact) en lista de contactos --> imprime cada uno de estos
        for contact in self._contacts:
            self._print_contact(contact)
            #se llama a esta funcion para hacerlo de forma mas ordenada

    def _print_contact(self, contact):
        print('----------------+----------------')
        print('Nombre: {}'.format(contact.name))
        print('Telefono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('----------------+---------------')

    def update(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                command = str(input('''
                Editar:
                    [n]ombre
                    [t]elefono
                    [e]mail
                    [to]do
                    '''))

                if command == 'n':
                    contact.name = str(input('Nombre nuevo: '))
                    print('LISTO!!!')
                    self._print_contact(contact)
                    self._save()
                    break

                elif command == 't':
                    contact.phone = str(input('Telefono nuevo: '))
                    print('LISTO!!!')
                    self._print_contact(contact)
                    self._save()
                    break

                elif command == 'e':
                    contact.email = str(input('Email nuevo: '))
                    print('LISTO!!!')
                    self._print_contact(contact)
                    self._save()
                    break

                elif command == 'to':
                    contact.name = str(input('Nombre nuevo: '))
                    contact.phone = str(input('Telefono nuevo: '))
                    contact.email = str(input('Email nuevo: '))

                    self._print_contact(contact)
                    self._save()
                    break
    
        else:
            print('Usuario no encontrado')
               
    def _save(self):
        with open('contacts.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow( ('name', 'phone', 'email'))

            for contact in self._contacts:
                writer.writerow( (contact.name, contact.phone, contact.email) )
        



def run():

    contact_book = ContactBook()
    
    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue

            contact_book.add(row[0], row[1], row[2])

    while True:
        command = str(input('''
            ¿Qué desas hacer?
            
            [a]ñadir contacto
            [ac]tualicar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contacto
            [s]alir

            '''))

        if command == 'a':
            name = str(input('Nombre del contacto: '))
            phone = str(input('Tel. del contacto: '))
            email = str(input('Email del contacto: '))

            contact_book.add(name, phone, email)

        elif command == 'ac':
            name = str(input('Nombre del contacto a editar: '))
            contact_book.update(name)

        elif command == 'b':
            name = str(input('Escribe el nombre del contacto a buscar: '))
            contact_book.search(name)

        elif command == 'e':
            name = str(input('Escribe el nombre del contacto a borrar: '))
            contact_book.delete(name)

        elif command == 'l':
            
            contact_book.show_all()
            
        elif command == 's':

            break
        else:
            print('Comando no encontrado.')

if __name__ == "__main__":
    print('           A G E N D A TRES-MIL')
    run()