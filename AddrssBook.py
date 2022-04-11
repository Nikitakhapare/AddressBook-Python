'''
@Author: Nikita
@Date: 2022-04-11 06: 30: 00
@Last Modified by:Nikita
@Last Modified time: 2022-04-11 06: 30: 00
@Title: Create Contact in Address Book
'''

class AddressBookUC1:
    
    def __init__(self, first_name, last_name, address, city, state, zip, phone, email) -> None:
        """
            Description:
                Function is Used getting values for object of AddressBook
            Parameter:
                Object with their specific data type
            Return:
                Updated Object as per our arguments
        """

        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone
        self.email = email


    def __str__(self):
        return "First Name is " + str(self.first_name) + "Last name is "+ str(self.last_name) + "Address is "+str(self.address) + "City is "+str(self.city) + "state is "+ str(self.city) + "Zip code is "+ str(self.zip)+"Phone no is "+str(self.phone) + "Email is "+ str(self.email)


if __name__=="__main__":
    cont1=AddressBookUC1("nikita","khapare","amravati","Amravati","Maharashtra",14986,9075194857,"nikitakhapare@gmail")
    print(cont1.__str__())
