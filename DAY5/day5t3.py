class car:
    def __init__(self,make,model,year,odometer=0):
        self.make=make
        self.model=model
        self.year=year
        self.odometer=0
    def drive(self,km):
        self.odometer+=km
    def get_info(self):
        print(f"make:{self.make}")
        print(f"model:{self.model}")
        print(f"year:{self.year}")
        print(f"odometer:{self.odometer}km")
c1=car("BMW","X5",2024)
c1.get_info()
c1.drive(150)
c1.drive(50)
print("/n after driving")
c1.get_info()