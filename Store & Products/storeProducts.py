class Store:
    def __init__(self,name):
        self.name = name
        self.list = []
    def add_product(self, new_product):
        self.list.append(new_product)
    def sell_product(self, id):
        self.list.pop(id)
    def inflation(self, percent_increase):
        for list in self.list:
            list.update_price(percent_increase,is_increased=True)
    def set_clearance(self, category, percent_discount):
        for list in self.products:
            if list.category == category:
                list.update_price(percent_discount, is_increased=False)
        
class Product:
    def __init__(self,name,price,category):
        self.name= name
        self.price =price
        self.category = category
    def update_price(self,percent_change,is_increased):
        if is_increased == True:
            self.price += self.price * percent_change
        else:
            self.price -= self.price * percent_change
    def print_info(self):
        print(f"Name: {self.name}\n Category: {self.category}\n price: {self.price}")
        

p = Product("Laptop", 1000, "Electronics")
p.print_info()
p.update_price(0.05, False)
p.print_info()
stor = Store("abd")
stor.add_product("cola")
