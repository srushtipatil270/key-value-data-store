import sys
sys.path.insert(1,'D:\python')
import CRD
from CRD import KeyValueBasedDataStore

d = KeyValueBasedDataStore()  # creates a new datastore instance

while(True):
    #choices for the user
    print("Press")
    print("1  to create a key value pair")
    print("2  to read a value for given key")
    print("3  to delete a key-value pair")
    print("4  to exit")
    
    ch = int(input("Enter your choice : "))
    
    if(ch == 1): #create a key value pair
        print()
        key = input("Enter Key : ")
        value = input("Enter value : ")
        timeout = int(input("Enter Timeout period(s) : "))
        print()
        d.Create(key,value,timeout)
        print()
        ch = 4
        
    if(ch == 2):  #read a value for given key
        print()
        key = input("Enter Key : ")
        print()
        d.Read(key)
        print()
        ch = 4
        
    if(ch == 3): #delete a key-value pair
        print()
        key = input("Enter Key : ")
        print()
        d.Delete(key)
        print()
        ch = 4
        
    if(ch == 4): #exit
        c = input("Want to continue? Y/N : ")
        if(c == "n" or c == "N"):
            break
    
    
