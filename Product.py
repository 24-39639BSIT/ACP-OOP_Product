class Product:
    inventory = []
    product_counter = 0

    def __init__(self, product_id, name, category, quantity, price, supplier):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.supplier = supplier

    @classmethod
    def add_product(cls, name, category, quantity, price, supplier):
        cls.product_counter += 1
        new_product = Product(cls.product_counter, name, category, quantity, price, supplier)
        cls.inventory.append(new_product)
        return "Product added successfully"
    
    @classmethod
    def delete_product(cls, product_id):
        for product in cls.inventory:
            if product.product_id == product_id:
                cls.inventory.remove(product)
                return "Product removed"
        return "Product not Found"
    
    @classmethod
    def update_product(cls, product_id, quantity = None, price = None, supplier = None):
        for product in cls.inventory:
            if product.product_id == product_id:
                if product.quantity is not None:
                   product.quantity = quantity
                if product.price is not None:
                   product.price = price
                if product.supplier is not None:
                   product.supplier = supplier
                return "Product Updated"
            return "No Product Found"  

class Order:
    
    def __init__(self, order_id, product_id, quantity, customer_info):
        self.order_id = order_id
        self.product_id= product_id
        self.quantity = quantity
        self.customer_info = customer_info

    def place_order(self):
        for product in Product.inventory:
            if product.product_id == self.product_id:
                return f"Product Ordered. Order ID: {self.product_id}"
        return "No Product Found"
    
p1 = Product.add_product("Laptop", "Electronics", 50, 1000, "Supplier A")
p2 = Product.add_product("T-Shirt", "Clothing", 100, 25, "Supplier B")
p3 = Product.update_product(1, quantity=45, price=950)
p4 = Product.delete_product(2)
order1 = Order(order_id=1, product_id=1, quantity=2, customer_info="John Doe")


print(p1)
print(p2)
print(p3)
print(p4)
print(order1.place_order())










