class Alpha:
    def function_a(self):
        print("Function A from Alpha class")
class Beta(Alpha):
    def function_b(self):
        print("Function B from Beta class")
class Gamma(Beta):
    def function_c(self):
        print("Function C from Gamma class")
        
g = Gamma()
g.function_a()  #Inherited from Alpha
g.function_b()  #Inherited from Beta
g.function_c()  #Own method of Gamma