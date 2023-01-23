#demonstrate instantiating a class

class real_estate:

    # Simple class
    # attribute
    attr1 = 'QWE123'
    attr2 = 'house'

    # sample method
    def property(self):
        print("It's Id:", self.attr1)
        print("It's a", self.attr2)

# Driver code
# Object instantiation
flat_no_1 = real_estate()

# Accessing class attributes
# and method through objects
print(flat_no_1.attr1)
flat_no_1.property()
