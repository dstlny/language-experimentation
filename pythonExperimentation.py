class notObject():
    
    def setName(self, name):
        self.name = name
    def setAddress(self, address):
        self.address = address
    def setPhoneNo(self, phone):
        self.phone = phone
    def setAge(self, age):
        self.age = int(age)
    def setDOB(self, dob):
        self.DOB = dob
    def setCountry(self, country):
        self.country = country
    def printInformation(self):
        print("Name: " + self.name + "\nAddress: " + self.address,
            "\nTelephone Number: ", self.phone + 
            "\nAge: " + self.age + "\nDate of birth: " + self.DOB,
            "\nCountry: " + self.country)

class personObject():

    def __init__(self, name, address, phone, age, dob, country):
        self.name = name
        self.address = address
        self.phone = phone
        self.age = age    
        self.DOB = dob
        self.country = country
    def displayPerson(self):
        print("Name: " + self.name, "\nAddress: " + self.address + 
            "\nTelephone Number: " + self.phone,
            "\nAge: " + self.age + "\nDate of birth: " + self.DOB,
            "\nCountry: " + self.country)

if __name__ == "__main__":
        
    var = input("Choose What you would like to do.\n1.Create a person (enter `01`, object orientated)\n2.Input your personal details (enter `02`, setting via functions)\nEnter: ")
    choice = var
        
    if choice == "01":
        var = input("Enter a name: ")
            
        while var.isnumeric() == True  or var == "": 
            var = input("Enter a valid name: ")
 
        name = var
        var = input("Enter an address: ")
        address = var
        var = input("Enter a telno: ")
    
        while var.isnumeric() == False or var == "" or len(var) < 11: 
            var = input("Enter a valid telno: ")
                
        telno = var   
        var = input("Enter an age: ")
            
        while var.isnumeric() == False or var == "": 
            var = input("Enter a valid age: ")

        age = var 
        var = input("Enter a date of birth in format 'dd/mm/yyyy' : ")
        dob = var
            
        if dob is None or dob.isalpha() == True: 
            dob = "02/03/1999"
            
        var = input("Enter a country: ")
        country = var
        e = personObject(name, address, telno, age, dob, country)
        e1 = personObject("Luke Elam", "Thing Street", "34847545435", "20", "02/03/1999", "United Kingdom")
        e2 = personObject("Test User", "Test test street", "04573456325", "69", "31/02/1999", "France")
        print("------User-created person object below------")
        e.displayPerson()
        print("------Pre-created person object below------")
        e1.displayPerson()
        print("------Pre-created person object below------")
        e2.displayPerson()
    elif choice == "02":
        m = notObject()
        var = input("Enter your name: ")
        m.setName(var)
        var = input("Enter your address: ")
        m.setAddress(var)
        var = input("Enter your telno: ")
        m.setPhoneNo(var)
        var = input("Enter your age: ")
        m.setAge(var)
        var = input("Enter your DOB: ")
        m.setDOB(var)
                   
        if var is None:
            print("Please enter your details")
        else:
            var = input("Enter your country please: ")  
            m.setCountry(var)
            m.printInformation()
    else:
        print(var + " is not a supported operation")
