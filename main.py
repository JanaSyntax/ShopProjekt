from checkout import checkout
from products import print_products, select_product
from cart import add_product_to_cart, show_cart, calculate_cart
from users import start_login_process, logout

def main():
    print("Willkommen im Shop!")
    start_login_process()

    while True:
        print("\n--- Menü ---")
        print("1 - Produkt hinzufügen")
        print("2 - Warenkorb anzeigen")
        print("3 - Checkout durchführen")
        print("4 - Abmelden und beenden")

        auswahl = input("\nIhre Auswahl: ")

        # todo call funtion from cart
        if auswahl == "1":
            print_products()
            produkt = select_product()
            if produkt:
                add_product_to_cart(produkt)
                print(f"{produkt['name']} wurde hinzugefügt!")

        elif auswahl == "2":
            show_cart()

        elif auswahl == "3":
            checkout()

        elif auswahl == "4":
            logout()
            print("Auf Wiedersehen!")
            break

        else:
            print("Ungültige Eingabe!")
