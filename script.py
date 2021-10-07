'''
INITIALIZE empty list grocery_inventory
SET products = file products.txt

'''
grocery_inventory = []
products = "products.txt"

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
    print ("")
    print (product_index['name'])
    print ("")
    print (f"This item costs ${product_index['cost']}")
    print (f"We have {product_index['qty']} in stock.")
    print ("")

'''
FUNCTION search(product_search):

    FOR items in grocery_inventory:
        IF product_search IN item:
            display_product (product_name)
'''



def search():
    
    user_input = input("Search for a product:  ")

    for d in grocery_inventory:
        if user_input in d['name']:
            #print (d['name'])
            #continue
            display_product(d)
            continue

        #elif user_input not in grocery_inventory:
        #    print ("")
        #    print("It looks like we don't have any items that match your search.")
        #    print("Try again.")
        #    print("")
        #    search()


'''
Open the grocery store!
'''

load_data(products)
#print(grocery_inventory)

print ("")
print ("Welcome to Internet Produce!")
print ("Your not so specialist grocer.")
print ("")
print ("Get started by searching for a product below.")
search()

