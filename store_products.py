class Store:
    
    def __init__(self,name):
        self.name = name
        self.product_lst = []

    def __repr__(self):
        return f"The products in the store are {repr(self.product_lst)}"

    def add_product(self, new_product):
        self.product_lst.append(new_product)
        return self

    def sell_product(self, id):
        self.product_lst.remove(self.product_lst[id])
        return self


class Product:
    
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category

    def __repr__(self) -> str:
        return f"{self.name} = ${self.price}"
    
    def update_price(self, percent_change, is_increase = True):
        if is_increase == True:
            self.price = (self.price * (percent_change / 100)) + self.price
        else:
            self.price = self.price - (self.price * (percent_change / 100))
    
    def print_info(self):
        return self.price, self.name, self.category

apple = Product('apple',3,'fruit')
orange = Product('orange',4,'fruit')
banana = Product('banana',2,'fruit')

walmart = Store('Walmart')

walmart.add_product(apple).add_product(orange).add_product(banana)

print(repr(walmart))