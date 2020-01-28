#Ryan Dalton - Week 5 - Pizza Factory Pattern

"""
Created pizza factory object that can take several parameters to create either specialty pizzas with predetermined
toppings or create custom pizzas.  Size, crust and toppings are taken into account.  Pizzas also generate their
base price based on number of toppings / crust and size.

Pizza factory puts all this together.
"""

class Pizza():
    def __init__(self, *toppings):
        self.size = "Large"
        self.crust = "Hand-Tossed"
        self.name = "CUSTOM"
        self.toppings = list(toppings)
        self.price = 10 + len(list(toppings))
        
    def __str__(self):
        return "{0}, {1}, {2} pizza with ".format(self.size, self.crust, self.name) + self.nameToppings()
    
    def repriceForSize(self):
        if self.size.lower() == "medium" or self.size.lower() == "md":
            self.size = "Medium"
            self.price = self.price - 2
        elif self.size.lower() == "small" or self.size.lower() == "sm":
            self.size = "Small"
            self.price = self.price - 4
        else:
            self.size = "Large"
            return 
    
    def nameToppings(self):
        pizzaString= ""
        if self.toppings == [""] or self.toppings == [" "]:
            self.toppings[0] = "cheese"
        numToppings = len(self.toppings)
        if numToppings > 1:
            i = 0
            while i != (numToppings - 1):
                pizzaString = pizzaString + self.toppings[i] + ", "
                i = i + 1
            pizzaString = pizzaString + "and {}.".format(self.toppings[-1])
            return pizzaString
        #For 1 topping only
        elif numToppings == 1:
            return "only " + self.toppings[0] + "."
        else:
            return "just cheese."

#Create subclasses with crusts
class ThinCrust(Pizza):
    def __init__(self, *args):
        super().__init__(*args)
        self.crust = "Thin Crust"
        self.price = self.price - 2
        
class DeepDish(Pizza):
    def __init__(self, *args):
        super().__init__(*args)
        self.crust = "Deep Dish"
        self.price = self.price + 2
        
class Calzone(Pizza):
    def __init__(self, *args):
        super().__init__(*args)
        self.crust = "Calzone Style"
        self.price = self.price - 4
        self.name = ""
        
class Stuffed(Pizza):
    def __init__(self, *args):
        super().__init__(*args)
        self.crust = "Stuffed"
        self.price = self.price + 6

#Create our factory
class PizzaFactory():
    #method to create custom pizzas
    #create custom handtossed
    def createCustom(self, size, crustType, *toppings):
        toppingList = toppings
        newPizza = self._createPizza(crustType, toppingList)
        newPizza.repriceForSize()
        return newPizza    
    
    #create with specialty string and size argument
    def create(self, size, crustType, specialty):
        #Possible crust types: handtossed, calzone, stuffed, thin crust, deep dish
        #Possible specialty strings: Supreme, Meat Lovers, Vegetarian, Hawaiian
        if specialty.lower() == "supreme":
            toppingList = ("Pepperoni", "Sausage", "Green Peppers", "Mushrooms", "Onions", "Olives")
        elif specialty.lower() == "meat lovers" or specialty.lower() == "meatlovers":
            toppingList = ("Pepperoni", "Sausage", "Salami", "Bacon")
        elif specialty.lower() == "vegetarian":
            toppingList = ("Spinach", "Artichokes", "Tomatoes", "Olives", "Onions", "Green Peppers")
        elif specialty.lower() == "hawaiian":
            toppingList = ("Canadian Bacon", "Pineapple")
        else:
            return "Unable to create pizza of specialty type: {}. Please retry.".format(specialty)
        newPizza = self._createPizza(crustType, toppingList)
        newPizza.size = size
        newPizza.repriceForSize()
        newPizza.name = specialty.upper()
        return newPizza
        
    #internal function to create various crust types and adjust price and object based on that
    def _createPizza(self, crustType, toppingList):
        if crustType.lower() == "handtossed":
            newPizza = Pizza(*toppingList)
        elif crustType.lower() == "deepdish":
            newPizza = DeepDish(*toppingList)
        elif crustType.lower() == "thincrust" or crustType.lower() == "thin crust":
            newPizza = ThinCrust(*toppingList)
        elif crustType.lower() == "calzone":
            newPizza = Calzone(*toppingList)
        elif crustType.lower() == "stuffed":
            newPizza = Stuffed(*toppingList)
        else:
            return "Unable to determine crust type. Please try again."
        return newPizza
        
        
def main():
    #test creation of basic pizza objects with increasing toppings
    #p = Pizza()
    #print(p)
    #p = ThinCrust("Pepperoni")
    #print(p)
    #p = DeepDish("Sausage", "Bacon")
    #print(p)
    #p = Calzone("Spinach", "Tomato", "Salami")
    #print(p)
    #p = Stuffed("Pepperoni", "Sausage", "Olive", "Pineapple")
    #print(p)
    #create pizza factory
    print("Testing Factory Pattern....\n")
    factory = PizzaFactory()
    #test use of factory to create specialty pizzas
    p1 = factory.create("medium", "deepdish", "supreme")
    p2 = factory.create("large", "thin crust", "vegetarian")
    p3 = factory.create("small", "calzone", "meatlovers")
    p4 = factory.create("large", "stuffed", "hawaiian")
    for i in [p1, p2, p3, p4]:
        print(i)
    #test use of factory createCustom method
    pp1 = factory.createCustom("Large", "deepdish", "pepperoni", "sausage")
    pp2 = factory.createCustom("Medium", "thin crust", "olive", "anchovie", "pineapple", "tomato")
    pp3 = factory.createCustom("Small", "handtossed", "spinach", "chicken", "bacon")
    pp4 = factory.createCustom("Medium", "calzone", "ricotta", "spinach", "arugla")
    for i in [pp1, pp2, pp3, pp4]:
        print(i)
    
main()
