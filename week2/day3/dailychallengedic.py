# Exercises 1
def create_letter_dict(word):
    letter_dict = {}
    
    for i, letter in enumerate(word):
        if letter not in letter_dict:
            letter_dict[letter] = []
        letter_dict[letter].append(i)
    
    return letter_dict

word = input("Enter a word: ")

result_dict = create_letter_dict(word)

print(result_dict)

# Exercises 2
def items_affordable(wallet, items_purchase):
    wallet = int(wallet.replace("$", "").replace(",", ""))
    
    affordable_items = []


    for item, price in items_purchase.items():
        item_price = int(price.replace("$", "").replace(",", ""))
        if wallet >= item_price:
            item_price -= wallet
            affordable_items.append(item)
    
    print(f"I have in my wallet ${item_price}")
    
    if affordable_items:
        return sorted(affordable_items)
    else:
        return "Nothing"

items_purchase = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20"
}

wallet = "$300"

result = items_affordable(wallet, items_purchase)
print(result)

items_purchase = {
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2"
}

wallet = "$100" 

result = items_affordable(wallet, items_purchase)
print(result)

items_purchase = {
  "Phone": "$999",
  "Speakers": "$300",
  "Laptop": "$5,000",
  "PC": "$1200"
}

wallet = "$1" 

result = items_affordable(wallet, items_purchase)
print(result)








