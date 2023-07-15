class store:
    def __init__(self,name, age, address, birthday, room):
        self.__name = name.upper()
        self.__age = age
        self.__address = address.upper()
        self.__birthday = birthday
        self.__room = room.upper()

    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get__address(self):
        return self.__address
    def get_birthday(self):
        return self.__birthday
    def get_room(self):
        return self.__room
    
    def keep(self):
        personal_info = open('Stored Informations.txt', 'a')
        personal_info.write("Name: "),personal_info.write(self.__name), personal_info.write('\n')
        personal_info.write("Age: "),personal_info.write(str(self.__age)), personal_info.write('\n') 
        personal_info.write("Birthday: "),personal_info.write(str(self.__birthday)), personal_info.write('\n')
        personal_info.write("Address: "),personal_info.write(str(self.__address)), personal_info.write('\n')
        personal_info.write("Room: "),personal_info.write(str(self.__room)), personal_info.write('\n'), personal_info.write('\n') 
        personal_info.close()
    
    def show(self):
        print("Name: ", self.__name) 
        print("Age: ", self.__age) 
        print("Address: ", self.__address)
        print("Birthday: ", self.__birthday)
        print("Room Number: ", self.__room)

s1 = store('Emanoel M. Quitong', '20', '69 Sitio Pulong Banal, Brgy. San Jose. Antipolo, Rizal', 'April 23,2003', '404')
s1.show()
s1.keep()