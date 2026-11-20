class Product:
    VAT_RATE = 0.15
    def __init__(self,code,name, price,stock):
        self.code = code
        self.name = name
        #needed for selling the product
        if stock < 0:
            raise ValueError("Quantity cannot be negative")
        self.stock = stock
        
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.price = price
        
    def __str__(self):
        return f"{self.code} - {self.name}: R{self.price:.2f}"
    
    def calc_vat(self):
        return self.price * self.VAT_RATE
    
    def price_including_vat(self):
        return self.price + self.calc_vat()
    
    def apply_discount(self, percentage):
        discount = self.price * percentage/100
        return self.price - discount
    
    def sell_product(self, quantity):
        if quantity > self.stock:
            
            return "Not enough stock, try a lesser amount"
        else:
            self.stock -= quantity
            return f"You bought {quantity} {self.name}s"
def main():
        product1 = Product("P001","Keyboard",450.00,20)
        product2 = Product("P002","Mouse",250.00,20)
        
        print(product1)
        print(product2)
        
        print("VAT: ", product1.calc_vat())
        print("Price including VAT: ", product1.price_including_vat())
        print("Price after 10% discount:", product1.apply_discount(10))
        print(product2.sell_product(10))
main()