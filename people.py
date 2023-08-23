

import re

class address:
    """
    Initializes street, city, and state
    """
    def __init__(self, street, city, state):
        self.street = street
        self.city = city
        self.state = state

class employee:
    """
    Initializes first name, last name, address, and email
    """
    def __init__(self, string):
        names = parse_name(string)
        self.first_name = names[0]
        self.last_name = names[1]
        self.address = parse_address(string)
        self.email = parse_email(string)
        

def parse_name(text):
    """
    Collects names from the line passed into it and returns a tuple with the first and last name.
    """    
   
    name_list = re.split("\s", text)    
    fname = name_list[0]
    lname = name_list[1]
    tuple = (str(fname), str(lname))
    return (tuple)
        

def parse_address(text):
    """
    Collects the address from the line passed into it and returns a string of the full address.
    """
    


    return ()


def parse_email(text):
    """
    Collects the email from the end of the line passed into it and returns the email
    """
    email = re.compile(r"[\d-]+$").search(text)[1]

    return (email)


def main(path):
    employee_list = []
    txt = open(path , 'r')

    while True:        
        line = txt.readline() 
        if not line: 
            break

        i = employee(line)
        employee_list.append(i)
        
    print('Length of employee_list = '+ str(len(employee_list)))
    print(employee_list)
    
if __name__ == "__main__":
    main('people.txt')