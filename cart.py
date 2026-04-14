from products import print_products, select_product


# cart als leere liste
cart = []


# reads user input and adds product to cart in loop
# input index, product name, price
def add_product_to_cart():
    while True:
        print_products()
        number = input(f"Bitte wähle ein Produkt aus. ")
        product = select_product(number)
        cart.append(product)
        while True:
            cancel = False
            answer = input("Möchtest du ein weiteres Produkt hinzufügen? \n'j' für Ja\n'n' für Nein")
            if answer == "j":
                break
            elif answer == "n":
                cancel = True
                break
            else:
                print("Fehlerhafte Eingabe. Bitte versuche es erneut.")
                continue
        if cancel == True:
            break


# print cart
# no output
def show_cart():
    for product in cart:
        print(product["name"], product["price"])
        

# calculates cart price sum
# output summe der preise
def calculate_cart():
    sum_cart = 0
    for product in cart:
        sum_cart += product["price"]
    return sum_cart
