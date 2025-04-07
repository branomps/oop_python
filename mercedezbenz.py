class MercedezBenz:
    doors=4
    model='G'
    wheels=4

    def __init__(self,color):
        self.color = color

    def drive(self):
        return f"A Mercedez is driving. It is {self}\n"
    
    def auto_drive(self):
        return "Auto is driving"
    
m1 = MercedezBenz("red")
print(f"The Mercedez is: {m1.color}")