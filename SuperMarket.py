shopping_list = ["banana", "orange", "apple"]
       
stock = {     
    "banana": 6, 
    "apple": 0,      
    "orange": 32,  
    "pear": 15       
}   
    
price = {
    "banana": 4, 
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

def compute_bill(food):
    #Calculate the total bill for the items in the shopping list
    total = 0
    for item in food:
        if stock[item] > 0:
            total += price[item]
            stock[item] -= 1
    return total

print (compute_bill(shopping_list))
