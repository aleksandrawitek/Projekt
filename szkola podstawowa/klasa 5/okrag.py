from math import pi
class Kolo():
    def __init__(self, r):
        self.radius = r
  

    def pole(self):
        return (self.radius**2)*pi 
    
    def obwod(self):
        return 2*self.radius*pi

