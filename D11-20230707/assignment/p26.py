print("Ye Olde Keychain Shoppe")
options=input("\n1. Add Keychains to Order\n2. Remove Keychains from Order\n3. View Current Order\n4. Checkout")
def add_keychains():
    print("\nADD KEYCHAINS\n",options)




def remove_keychains():
    print("\nREMOVE KEYCHAINS\n",options)



def view_order():
    print("\nVIEW ORDER\n",options)



def checkout():
    print("\nCHECKOUT",options)
    



choice=int(input("\nPlease enter your choice: "))
if(choice==1):
    add_keychains()

elif(choice==2):
    remove_keychains()

elif(choice==3):
    view_order()

elif(choice==4):
    checkout()

