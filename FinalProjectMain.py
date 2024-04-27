"""
Interactive Inventory Query Capability


"""
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


    def __init__(self,manfac,itemType): #initiaze the manufacturer and Item tupe to be use in other functions
        self.manfac = manfac
        self.itemType = itemType

    def queryUser(self): #add check price 
        
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
    
   

    for key,value in Inventory.filterInventory.items():
            if key == inventoryStuff.queryUser():
              print(f"Your item is: {key},{value[0]},{value[1]},{value[2]}")
              thisKey = key
    
    
    for key,value in Inventory.filterInventory.items():
        if itemType in Inventory.filterInventory.get(key) and key != thisKey: 
            print(f"You many also like: {key},{value[0]},{value[1]},{value[2]}")
           
    

if __name__ == "__main__":
    main()
