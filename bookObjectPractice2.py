class Blanket:
    def __init__(self, soft, color):
        self.soft = soft
        self.color = color

    def softness(self):
        print (f"This blanket looks {self.soft}!")
        
    
    def show_color(self):
        print (f"This blanket is {self.color}!")

blanket1 = Blanket("very soft", "green")
blanket2 = Blanket("rough", "black")

blanket2.softness()