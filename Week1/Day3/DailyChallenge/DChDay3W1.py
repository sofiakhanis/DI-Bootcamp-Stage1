#exercise 1

user_inp = input("Enter a word (of 10 characters max): ")

if len(user_inp) > 10: #to specify the amount of characters 
    print ("No! The word is too long, try again.")
    user_inp = input("Enter a word: ")

char_dict = {}
for ind, char in enumerate(user_inp): 
    if char in char_dict:
        char_dict[char].append(ind)
    else:
        char_dict [char] = [ind]

print (char_dict)

#exercise 2

items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}

wallet = "$300"

wallet_amount = int(wallet.replace("$", "").replace(",", "")) #cleaning data

affordable_items = []

for item, price in items_purchase.items(): 
    item_price = int(price.replace("$", "").replace(",", ""))
    if item_price <= wallet_amount: #checking if can afford
        affordable_items.append(item)

affordable_items.sort() #sorting
if affordable_items:
    print(affordable_items)
else:
    print("Nothing")
