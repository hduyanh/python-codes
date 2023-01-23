
class car:

    # init method or constructor
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def show(self):
        print("Model is", self.model)
        print("Color is", self.color)

# both objects have different self which contain their attributes
audi = car("audi a4", "blue")
ferrari = car("ferrari 488", "green")

# Method 1
audi.show()     # same output as car.show(audi)
ferrari.show()  # same output as car.show(ferrari)

# Method 2
print("Model for audi is", audi.model)
print("Color for ferrari is", ferrari.color)