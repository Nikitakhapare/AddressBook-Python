'''
@Author: Nikita
@Date: 2022-04-11 03: 15: 00
@Last Modified by:Nikita
@Last Modified time: 2022-04-11 03: 15: 00
@Title: Add Contact in Address Book
'''

class AddressBook:
    def __init__(self):
        """
            Description:
                Function is Used getting values for object of AddressBook
            Parameter:
                Object with their specific data type
            Return:
                Updated Object as per our arguments
        """

        self.first_name = " "
        self.last_name = " "
        self.address = " "
        self.city = " "
        self.state = " "
        self.zip = " "
        self.phone = " "
        self.email = " "
        self.list=[]

    
    def add_contact(self):
        """
        Description:
            Function is Used for taking Proper input from User with given parameters
        Parameter:
            self parameter
        Return:
            Object Create with given parameters
        """
        first_name = input('first name: ')
        self.list.append(first_name)
        last_name = input('lastName: ')
        self.list.append(last_name)
        address = input('address: ')
        self.list.append(address)
        city = input('city: ')
        self.list.append(city)
        state = input('state: ')
        self.list.append(state)
        zip = int(input('zip: '))
        self.list.append(zip)
        phone =int( input('phone :'))
        self.list.append(phone)
        email = input('email: ') 
        self.list.append(email)  


    def display_contact(self):
        """
        Description:
            Display the list .
        Parameter:
            self is as parameter
        Return:
            Returning nothing but printing the list.
        """
        contact= {}
        contact_length = len(contact)
        print(contact_length)
        contact[contact_length] = self.list
        print(contact)

    


    def main(self):
        print('Enter 1. To Add Contacts 2. For display a Contact 3.for Exist')
        while True:
            choice = int(input('Enter your choice: '))
            if choice == 1:
                self.add_contact()
            elif choice == 2:
                self.display_contact()
            elif choice== 3:
                exit()
            else:
                print('Invalid Option. Try Again!')



if __name__ == "__main__":
    addressBook = AddressBook()
    addressBook.main()
