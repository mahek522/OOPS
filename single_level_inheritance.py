class Alpha:
    def function(self):
        print("Alpha class function called")
class Beta(Alpha):
    pass
b=Beta()
b.function()  #Inherited method from Alpha class
print(dir(Alpha)) #List attributes and methods of Alpha class