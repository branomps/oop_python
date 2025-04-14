class Tire:
    def __init__(self,kind,distance_covered):
        self.kind = kind
        self.distance_covered = distance_covered


class MercedezBenz:
    doors=4
    model='G'
    wheels=4
    tires = [Tire("operational", 10 ) for i in range(4)]

    def __init__(self,color):
        self.color = color

    def drive(self):
        return f"A Mercedez is driving. It is {self}\n"
    
    @staticmethod
    def auto_drive():
        return f"Auto is driving\n"
    
    @classmethod
    def create_lease(cls):
        print(f"A lease for {cls} will be created")
    
m1 = MercedezBenz("red")
print(f"The Mercedez is: {m1.color}")

m2 = MercedezBenz("blue")

print(m2.auto_drive())

print(m2.tires ,"\n")