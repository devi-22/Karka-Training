print("Ye Olde Keychains Shoppe")
def add_keychains():
    global cart
    cart=0
    ques1=int(input(f"\nYou have {cart} keychains. How many to add?"))
    cart=cart+ques1
    print(f"You now have {cart} keychains")
    return cart
def remove_keychains(cart):
    ques2=int(input(f"\nYou have {cart} keychains. How many to remove?"))
    cart=cart-ques2
    print(f"You now have {cart} keychains.")
    return cart
def view_order(cart):
    order=cart*10
    print(f"\nYou have {cart} keychains.\nKeychains cost is 10 each.\nTotal cost is {order}.")
    return cart
def checkout():
    name=input("What is your name?")
    order=cart*10
    print(f"\nYou have {cart} keychains.\nKeychains cost is 10 each.\nTotal cost is {order}.\nThanks for your order, {name}.")
    return cart
while True:
    print("\n1. Add Keychains to Order\n2. Remove Keychains from Order\n3. View Current Order\n4. Checkout")
    choice=int(input("\nPlease enter your choice: "))
    if (choice==1):
        cart=add_keychains()
    elif (choice==2):
        cart=remove_keychains((cart))
    elif (choice==3):
        cart=view_order((cart))
    elif (choice==4):
        cart=checkout()
        break






