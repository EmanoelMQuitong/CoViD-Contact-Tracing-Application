class store:
    def __init__(self,name, birthday,status, address, room, Vaccination, Symptoms, Exposure, Covid_contact, Covid_test, CP_Name, CP_Relationship, CP_Contact_number, CP_Email_address):
        self.__name = name.upper()
        self.__address = address.upper()
        self.__birthday = birthday.upper()
        self.__room = room.upper()
        self.__status = status.upper()
        self.__Vaccination = Vaccination.upper()
        self.__Symptoms = Symptoms.upper()
        self.__Exposure = Exposure.upper()
        self.__Covid_contact = Covid_contact.upper()
        self.__Covid_test = Covid_test.upper()
        self.__CP_Name = CP_Name.upper()
        self.__CP_Relationship = CP_Relationship.upper()
        self.__CP_Contact_number = CP_Contact_number
        self.__CP_Email_address = CP_Email_address

    #Get parameters
    def get__CP_Email_address(self):
        return self.__CP_Email_address
    def get__CP_Contact_number(self):
        return self.__CP_Contact_number
    def get__CP_Relationship(self):
        return self.__CP_Relationship
    def get__CP_Name(self):
        return self.__CP_Name
    def get__Covid_test(self):
        return self.__Covid_test
    def get__Covid_contact(self):
        return self.__Covid_contact
    def get__Exposure(self):
        return self.__Exposure
    def get_Symptoms(self):
        return self.__Symptoms
    def get_Vaccination(self):
        return self.__Vaccination
    def get_status(self):
        return self.__status
    def get_name(self):
        return self.__name
    def get_birthday(self):
        return self.__birthday
    def get__address(self):
        return self.__address
    def get_room(self):
        return self.__room
    
    def keep(self):
        personal_info = open('Stored Informations.txt', 'a')
        personal_info.write(self.__name), personal_info.write('\n')
        personal_info.write(str(self.__birthday)), personal_info.write('\n')
        personal_info.write(str(self.__status)), personal_info.write('\n')
        personal_info.write(str(self.__address)), personal_info.write('\n')
        personal_info.write(str(self.__room)), personal_info.write('\n')
        personal_info.write(str(self.__Vaccination)), personal_info.write('\n') 
        personal_info.write(str(self.__Symptoms)), personal_info.write('\n')
        personal_info.write(str(self.__Exposure)), personal_info.write('\n')
        personal_info.write(str(self.__Covid_contact)), personal_info.write('\n')
        personal_info.write(str(self.__Covid_test)), personal_info.write('\n')
        personal_info.write(str(self.__CP_Name)), personal_info.write('\n')
        personal_info.write(str(self.__CP_Relationship)), personal_info.write('\n')
        personal_info.write(str('+63 ')),personal_info.write(str(self.__CP_Contact_number)), personal_info.write('\n')
        personal_info.write(str(self.__CP_Email_address)), personal_info.write('\n'), personal_info.write('\n') 

        personal_info.close()
    
    

