import random #Function to choose a random thing from the list
food=["cauliflower", "tilapia fillet", "pork loin", "green beans", "rainbow carrots", "potatoes", "three color squash","eggplant","baguette"] # List 
preperations=["with balsamico", "with garlic and olive oil", "with minted yogurt", "soup", "chutney", "salad", "with salsa", "over sticky rice","au jus", "with basmati rice"] #List 
items=input("how many items would you like? ") # Printing how many items would you like
for number in range(int(items)): # for number in the list choose a random item
    print(random.choice(food)+" "+random.choice(preperations)) # telling it to print one item from the food at random and one from preperations and put them togehter. 
    
