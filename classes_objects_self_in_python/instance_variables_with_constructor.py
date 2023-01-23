# Class for Property

class Property:

    # Class Variable
    status_1 = 'Sold'
    status_2 = 'Available'

    # The init method or constructor
    def __init__(self, area, type):
        
        # Instance Variable
        self.area = area
        self.type = type

# Objects of Property class
property_number_1 = Property("100 square meter", "house")
property_number_2 = Property("50 square meter", "flat")

print("Property number 1 details:")
print("Status:", Property.status_1)
print("Area:", property_number_1.area)
print("Type:", property_number_1.type)

print("\nProperty number 2 details:")
print("Status:", Property.status_2)
print("Area:", property_number_2.area)
print("Type:", property_number_2.type)

# Class variables can be accessed using class name also
print("\nAccessing class variable using class name")
print(Property.status_1)
print(Property.status_2)