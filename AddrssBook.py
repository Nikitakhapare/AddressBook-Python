'''
@Author: Nikita
@Date: 2022-04-11 03: 15: 00
@Last Modified by:Nikita
@Last Modified time: 2022-04-11 03: 15: 00
@Title: Add Contact in Address Book
'''

class AddressBook:
    
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
            last_name = input('lastName: ')
            address = input('address: ')
            city = input('city: ')
            state = input('state: ')
            zip = input('zip: ')
            phone = input('phone :')
            email = input('email: ')   

            return (first_name, last_name, address, city, state, zip, phone, email)



if __name__ == "__main__":
    addressBook = AddressBook()
    contact_list=[] 
    flag=True
    while True:
        cont1=addressBook.add_contact()
        contact_list.append(cont1)
        n=int(input("Enter 1 to continue ")) 
        if n==1:
            continue
        if n==0:
            Flag=False

        print(contact_list)


