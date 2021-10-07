'''
INITIALIZE empty list grocery_inventory
SET products = file products.txt

'''
grocery_inventory = []
products = "products.txt"
art = "grocery_art.txt"


'''
Fucntion LOAD ART loads the ascii art file.
It removes the line break at the end of each line and prints each line to show the art.
'''

def load_art(filename):
    file = open(filename, "r")
    lines = file.readlines()
    for line in lines:
        art_line = line.replace("\n", "")
        print (art_line)


'''
FUNCTION load_data(filename):

'''

def load_data(filename):
    file = open(filename, "r")
    lines = file.readlines()
    for line in lines:
        #print ("========================")
        #print(line)
        line = line.replace("\n", "")
        value = line.split(',') #split each line at the comma into a list
        #print (value)
        #print ("========================")
        product_name = value[1] #assign index 1 to the product name
        name = product_name #assign name to product name (mutability)
        #print(product_name)
        cost = value[2] #assign index 2 to the cost 
        qty = value[3] #assign index 3 to the qty

        #initalize an empty dictionary
        product_name = {}

        #append key-value pairs into the dictionary
        product_name ["name"]=name
        product_name["cost"]=cost
        product_name["qty"]=qty

        #print (product_name)

        #append the dictionary to the grocery_inventory list
        grocery_inventory.append(product_name)
        #print(grocery_inventory)


    file.close()
    return grocery_inventory


'''
FUNCTION display_product(product_name):
    DISPLAY product_name
    DISPLAY brand
    DISPLAY cost
    DISPLAY qty
    
'''

def display_product(product_index):
    #print ("DISPLAY FUNCTION")
    name = product_index['name']
    cost = product_index['cost']
    qty = product_index['qty']
    total = round((float(cost) * int(qty)), 2)
    print ("")
    print (name)
    print ("")
    print (f"This item costs ${cost}")
    print (f"We have {qty} in stock.")
    print ("")
    print (f"You can buy our entire inventory of {name} for a bargain price of ${total}!")
    print ("")

'''
FUNCTION search(product_search):

    FOR items in grocery_inventory:
        IF product_search IN item:
            display_product (product_name)
'''


def search():
    
    user_input = input("Search for a product:  ")
    valid_search = False

    #if they input inventory, show a list of all items in stock
    if user_input.lower() == "inventory":
        for d in grocery_inventory:
            print (d['name'])
        valid_search = True

    #otherwise, look to see if their input matches any groceries
    for d in grocery_inventory:
        if user_input.title() in d['name']:
            #print (d['name'])
            display_product(d)
            valid_search = True
            continue

    #if there are no items that match, print the following
    if valid_search == False:
        print ("")
        print("It looks like we don't have any items that match your search.")
        print("Try again.")
        print("")
        
    search_again()

'''
Create a function asking user if they want to search again
'''

def search_again():
    print("Would you like to search for another product?")
    user_input = input("yes/no --> ")

    if user_input.lower() == "yes":
        print("")
        search()

    elif user_input.lower() != "no":
        print("")
        print("Input not recognized.")
        search_again()



'''
Open the grocery store!
'''

load_data(products)
#print(grocery_inventory)

print ("")
load_art(art)
print ("")
print ("")
print ("Welcome to Internet Produce!")
print ("Your not so specialist grocer.")
print ("")
print ("Get started by searching for a product below or type")
print ("'inventory' at any time to see what's available")
print ("")
search()

