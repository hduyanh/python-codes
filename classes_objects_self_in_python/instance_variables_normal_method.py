# Create instance variables inside methods

# Class for Propterties

class real_estate:

    # Class Variable
    status = 'Sold'

    # The init method or constructor
    def __init__(self, type):

        # Instance Variable
        self.type = type
    
    # Add an instance variable
    def setLocation(self, location):
        self.location = location
    
    # Retrieves instance variable
    def getLocation(self):
        return self.location

# Driver Code
flat_number_1 = real_estate("house_1")
flat_number_1.setLocation("California")
print(flat_number_1.getLocation())