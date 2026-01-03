class DeliveryAgent:
    def __init__(self, name, rating, ph_no):
        self.name = name
        self.rating = rating
        self.ph_no = ph_no

class Restaurant:
    class FoodItem:
        def __init__(self, name, price, rating, is_veg):
            self.name = name
            self.price = price
            self.rating = rating
            self.is_veg = is_veg
    def __init__(self, name, addr, rating):
        self.name = name
        self.addr = addr
        self.rating = rating
        self.pizza = Restaurant.FoodItem("Pizza", 120, 4.5, False)
        
    def assign_delivery_agent(self, agent):
        self.agent = agent
def main():
    r = Restaurant("Foodies", "Blore", 4.2)
    steve = DeliveryAgent("Steve", 4.8, "1234567890")
    r.assign_delivery_agent(steve)
    print(f"Restaurant: {r.name}, Address: {r.addr}, Rating: {r.rating}")
    print(f"Food Item: {r.pizza.name}, Price: {r.pizza.price}, Rating: {r.pizza.rating}, Is Veg: {r.pizza.is_veg}")
    print(f"Delivery Agent: {r.agent.name}, Rating: {r.agent.rating}, Phone No: {r.agent.ph_no}")
    
    #print(pizza.name)  # This will raise an error as pizza is not defined in this scope
    #print(steve.name)  # This will raise an error as steve is not defined in this scope
    
if __name__ == "__main__":
    main()    