"""
Interactive Inventory Query Capability

    Query the user of an item by asking for manufacturer and item type.
        Print a message (“No such item in inventory”) if either the manufacturer or the item type is not in the inventory, more that one of either type is submitted or the combination is not in the inventory. Ignore any other words, so “nice Apple computer” is treated the same as “Apple computer”.
        Print “Your item is:” with the item ID, manufacturer name, item type, and price on one line. Do not provide items that are past their service date or damaged. If there is more than one item, provide the most expensive item.
        Also, print “You may, also, consider:” and print information about the same item type from another manufacturer that closes in price to the output item. Only print this if the same item from another manufacturer is in the inventory and is not damaged nor past its service date.
        After output for one query, query the user again. Allow ‘q’ to quit.


Using Classes is MANDATORY. 
Using Pandas is Prohibited. 

Commit all your .py files on GitHub.  Provide a link on Canvas. 

Name all your files starting with “FinalProject” for example FinalProjectInput.py

Comment your code extensively. 
p
"""

"Ask user for manufacture and Item type"
"make something that remove damaged and past service date items"


"1. "
from datetime import datetime

class Inventory: #This class takes user input of Manufactures and Items, finds them and suggest another item.

    #Main Dictionary that is not manipulated, only accessed 
    itemInventory = {5010421:['Dell','Laptop', 450,'03-19-22',''],
                 4310431:['Lenovo','Laptop',550,'02-10-23',''],
                 1239736:['Apple','Phone',600,'05-09-22',''],
                 3203683:['Samsung','Phone',550,'09-05-23',''],
                 2749573:['Dell','Desktop',500,'11-12-23','Damaged'],
                 5838037:['Apple','Desktop',700,'12-19-20','']   #I'm not sure exactly what you meant by past service date, so this item is before the cut off date 
                  }
    
    #Secondary Dictionary where Damaged and out of date items are removed 
    filterInventory = {}


    def __init__(self,manfac,itemType): #init
        self.manfac = manfac
        self.itemType = itemType

    def queryUser(self): #add check price 
        #self.manfac = input("Enter a manufacture: ")
        #self.itemType = input("Enter an item: ")

        '''

        for key,value in Inventory.itemInventory.items():
            if self.manfac in value and self.itemType in value:
                print(f"Here is your stuff {self.itemKey}")
                return key
                break
        
        else:
            print("That combo does not exit")
        '''
        for key,value in Inventory.filterInventory.items():
            if self.manfac in value and self.itemType in value:
                #print(f"Here is your stuff {key}")
                return key
                
        else:
            print("That combo does not exist")
            


    def userItemCleaner():  #items past service date or damaged 
        for key,values in Inventory.itemInventory.items():
             date_value = values[3]
             status_value = values[4]

             if status_value != 'Damaged' and (not date_value or (date_value and datetime.strptime(date_value, '%m-%d-%y') >= datetime.strptime('12-20-20', '%m-%d-%y'))):
                 Inventory.filterInventory[key] = values

        

        

    '''
    def considerItem(self):
        for key,value in Inventory.filterInventory.items():
            #self.itemType in Inventory.filterInventory.items():
            if Inventory.filterInventory.get(key) != Inventory.queryUser:
                print(f"You many also like: {key},{value[0]},{value[1]},{value[2]}")
            else:
                print("This is not working")
     '''

    def printing():
        '''
        for key,value in Inventory.filterInventory.items():
            if key == Inventory.queryUser:
              print(f"Your item is: {key},{value[0]},{value[1]},{value[2]}")
            else:
                print("something is wrong")
                break
        '''
    
        

    
#InventoryStuff = Inventory()
#InventoryStuff.queryUser()
#Inventory.queryUser()
#Inventory.queryManufacture()
#Inventory.queryItem()
#Inventory.itemChecker()
#Inventory.userItemCleaner()
#print(Inventory.filterInventory)

def main():

    #while input does not have "q"
    Inventory.userItemCleaner()

    manfac = input("Enter a manufacture: ")
    itemType = input("Enter an item: ")

    inventoryStuff = Inventory(manfac,itemType)
    #inventoryStuff.queryUser()
   

    for key,value in Inventory.filterInventory.items():
            if key == inventoryStuff.queryUser():
              print(f"Your item is: {key},{value[0]},{value[1]},{value[2]}")
              thisKey = key
    #inventoryStuff.considerItem()
    
    for key,value in Inventory.filterInventory.items():
        if itemType in Inventory.filterInventory.get(key) and key != thisKey: 
            print(f"You many also like: {key},{value[0]},{value[1]},{value[2]}")
           
    #Inventory.considerItem()         
            


    #Inventory.printing()
    #print(inventoryStuff.queryUser())

if __name__ == "__main__":
    main()
#stuff = Inventory