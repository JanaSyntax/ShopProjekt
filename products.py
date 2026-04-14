# product: {index, name, price}
# Liste von Produkten 
_listeVonProdukten = [
    {"name" : "Kamera von Marvin", "price": 5000 }, 
    {"name" : "Kondensatormikrofon", "price": 1000 }, 
    {"name" : "Mischpult", "price": 1500 }, 
    {"name" : "Spotstrahler", "price": 200 }, 
]


# print index numbers, product names and prices
# 1 - Auto
# 2 - Kaffeemaschine

def print_products():
    liste = _print_products_def();    
    for myprod in liste: 
        print(myprod) 

def _print_products_def():
    product_list = []
    i = 0
    for p in _listeVonProdukten: 
        product_list.append({"index": i, "name": p["name"], "preis": p["price"]});
        i = i + 1;
    return product_list  

    # code here

# produkt zu zahl zurückgeben
# input -> index number
# output -> produkt mit diesem index zurückgeben
def select_product(number):
    # code here
    print("bla") 


print_products();



