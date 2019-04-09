class option1():
    
    def setName(self, name):
        self.name = name
    def setAddress(self, address):
        self.address = address
    def setPhoneNo(self, phone):
        self.phone = phone
    def setAge(self, age):
        self.age = int(age)
    def setDOB(self,dob):
        self.DOB = dob
    def setCountry(self, country):
        self.country = country
    def printInformation(self):
        print("Name: " + self.name + "\nAddress: " + self.address,  
            "\nTelephone Number: ", self.phone +
            "\nAge: " + self.age +
            "\nCountry: " + self.country)

class option2():
    
    def __init__(self, name, address, phone, age, dob, country):
        self.name = name
        self.address = address
        self.phone = phone
        
        try: self.age = int(age) 
        except ValueError: print("Fuck.")
            
        self.DOB = dob
        self.country = country
        
    def displayPerson(self):
        print("Name:" + self.name,"\nAddress: "+ self.address+  
            "\nTelephone Number: "+ self.phone,
            "\nAge: "+ self.age+"\nDate of birth: "+ self.DOB, 
            "\nCountry: "+ self.country)
        
if __name__ == '__main__':
    var = input("Choose What you would like to do.\n1.Create a person (enter `01`, object orientated)\n2.Input your personal details (enter `02`, setting via functions)\nEnter: ")

    if var == "01":
        var = input("Enter a name: ")
        name = var
        var = input("Enter an address: ")
        address = var
        var = input("Enter a telno: ")
        telno = var
        var = input("Enter an age: ")
        age = var
        var = input("Enter a date of birth: ")
        dob = var
        var = input("Enter a date of country: ")
        country = var
        e = option2(name, address, telno, age, dob, country)
        e.displayPerson()
    elif var == "02":
        m = option1()
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
