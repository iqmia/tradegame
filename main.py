
class User:
    def __init__(self, name, products, quantity):
        self.name = name
        self.products = products
        self.quantity = quantity
        
        assert type(self.products)== list, "type not list"
        
        assert type(self.quantity)== list, "type not list"
    
    @property
    def totalmoney(self):
        
        prods = [p for p in self.products]
        quant = [q for q in self.quantity]
        prices = []
        totalnosum = []
        
        for m in range(len(prods)):
            prices.append(prods[m].findprice)
        
        for x in range(len(prods)):
            totalnosum.append(prices[x]*quant[x])
        
        total=sum(totalnosum)
        
        return f'{total} dollars'
    
    def __str__(self):
        
        prods = [p for p in self.products]
        quant = [q for q in self.quantity]
        userprods = []
        for h in range(len(prods)):
            userprods.append(prods[h].name)
   
        return f'Name: {self.name}, Products: {userprods}, Quantities of products: {quant}, Total balance: {self.totalmoney}'


    
class Product:
    
    def __init__(self, name, price, totalquantity):
        
        self.name = name
        self.price = price
        self.totalquantity = totalquantity
    
    @property                      
    def findprice(self):
        
        return self.price
    
    def falsecheck(self,User):
        
        pass


        
        
        
gold=Product('gold',5,10)  
iron=Product('iron',2,50)
elie=User('Elie Saad', [gold , iron], [2, 3])
karl=User('Karl Saad', [gold , iron], [3, 2])
print(elie)
print(karl)
