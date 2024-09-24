class Country:
    def acceptCountry(self):
      self.cname=input("enter the country name:")
    def dispCountry(self):
      print("Country name is :",self.cname)
class State(Country):
    def acceptState(self):
       self.sname=input("enter the state name:")
    def dispState(self):
      print("State name is :",self.sname)

obj=State()
obj.acceptCountry()
obj.acceptState()
obj.dispCountry()
obj.dispState()