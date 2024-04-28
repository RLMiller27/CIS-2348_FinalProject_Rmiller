"""
Interactive Inventory Query Capability 
Randell Miller 

MISSING FUNCTIONALITY: Program does not "provide most expensive item" and dose not provide "item that is closes in price" just a simailar item.

ERRORS: 1.Program will print "No such item in inventory for each item in the inventory when there is a miss match in user and dictionary selection.
        2.SQL injection like exploit if manufacture or item type are entered with the date allowing simalar answer (Dell, 03-19-22).
        3.The program will end when 'q' is entered, but it will state 'No such item in inventory' repeatedly
        4.'No such item in inventory' will print for each item in the dictionary when called
"""
from datetime import datetime

class Inventory: #This class takes user input of Manufactures and Items, finds them and suggest another item.

    #Main Dictionary that is not manipulated, only accessed, I'm not sure what the inputs were supposed to look like so I made my own
    itemInventory = {5010421:['Dell','Laptop', 450,'03-19-22',''],
                 4310431:['Lenovo','Laptop',550,'02-10-23',''],
                 1239736:['Apple','Phone',600,'05-09-22',''],
                 3203683:['Samsung','Phone',550,'09-05-23',''],
                 2749573:['Dell','Desktop',500,'11-12-23','Damaged'],
                 5838037:['Apple','Desktop',700,'12-19-20','']   #I'm not sure exactly what you meant by past service date, so this item is before the cut off date of '12-20-20'.
                  }
    
    #Secondary Dictionary where Damaged and out of date items are removed 
    filterInventory = {}


    def __init__(self,manfac,itemType): #initiaze the manufacturer and Item type to be use in other functions
        self.manfac = manfac
        self.itemType = itemType

    def queryUser(self): #calls user and checks if the item is the same as in the dictionary and returns key 
        
        for key,value in Inventory.filterInventory.items():
            if self.manfac in value and self.itemType in value:
                
                return key
                
        else:
            print("No such item in inventory")
            


    def userItemCleaner():  # removes items that are past service date or damaged 
        for key,values in Inventory.itemInventory.items():
             dates = values[3]
             isDamaged = values[4]

             if isDamaged != 'Damaged' and (not dates or (dates and datetime.strptime(dates, '%m-%d-%y') >= datetime.strptime('12-20-20', '%m-%d-%y'))):
                 Inventory.filterInventory[key] = values


def main(): # main function where user input is taken and keys are checked 

    
    Inventory.userItemCleaner()
    manfac = 0

    while manfac != 'q': #Error the program will end but it will state 'no such item in inventory' four times

        manfac = input("Enter a manufacture: ")
        itemType = input("Enter an item: ")

        inventoryStuff = Inventory(manfac,itemType)
    
   

        for key,value in Inventory.filterInventory.items(): # query user and check if key = user input key
                if key == inventoryStuff.queryUser():
                    print(f"Your item is: {key},{value[0]},{value[1]},{value[2]}")
                    thisKey = key
    
    
        for key,value in Inventory.filterInventory.items(): # outputs item if the key is different 
                if itemType in Inventory.filterInventory.get(key) and key != thisKey: 
                    print(f"You many also, consider: {key},{value[0]},{value[1]},{value[2]}")
           
    

if __name__ == "__main__":
    main()
