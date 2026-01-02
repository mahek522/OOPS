class Alpha:
    def function1(self):
        print("Alpha class function1 called")
class Beta:
    def function2(self):
        print("Beta class function2 called")
class Gamma(Alpha, Beta):
    pass
g = Gamma()
g.function1()  #Inherited from Alpha
g.function2()  #Inherited from Beta