class Auto:
    def __init__(self, marka, rocznik):
        self.marka = marka
        self.rocznik = rocznik
    
    def drive(self): 
        print(f"your {self.marka} is now driving")



auto = Auto("mercedes", 1994)
print(auto.marka)
auto.drive()