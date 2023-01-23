# Class with init method
class real_estate:

    # init method or constructor
    def __init__(self, type):
        self.type = type
    
    # Sample method
    def property_type(self):
        print("The property type:", self.type)

property_1 =  real_estate('house')
property_1.property_type()
