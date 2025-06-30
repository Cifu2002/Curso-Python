class Classy:
    def method(self):
        print("método")


obj = Classy()
obj.method()

class Classy:
    def __init__(self, value):
        self.var = value


obj_1 = Classy("objeto")

print(obj_1.var)
    