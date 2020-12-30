import time
import threading
import sys
import json

class KeyValueBasedDataStore:
    
    datastore = {} #datastore - to store key-value pairs
    data_id = 1
    
    def Create(self,key,value,timeout = 0):
        #creates a new key-value pair
        
        found = 0
        #checks whether key is already present
        for i in self.datastore:
            if(key in self.datastore[i]):
                found = 1
                break
        if(found == 1):
            print("Key already exist!!! Try again!")
            return
        
        #checks whether key is a string
        if(not(str(key).isalpha())) :
            print("Key must be string")
            return
        
        #checks whether
        #  1  datastore is not more than 1GB
        #  2  key is less than 32chars
        #  3  value is less than 16KB
        if(self.datastore.__sizeof__() >= 1024*1024*1024) or (len(key)>32) or (value.__sizeof__()>=(16*1024)):
            print("Memory limit Exceeded!!!!")
            return

        # stores new key-value pair 
        self.datastore[self.data_id] = {}   
        self.datastore[self.data_id][key] = json.dumps(value)  # converts value to json object and stores
        self.datastore[self.data_id]["timeout"] = time.time()+(timeout*1000)  # timeout is stored along with key-value pair 
        self.data_id += 1
        
        print("Created '"+str(key)+"' : '"+str(value)+"' successfully")

    def Read(self,key):
        #reads value for given key
        
        found = 0
        #finds key in the datastore
        for i in self.datastore:
            if(key in self.datastore[i]):
                found = 1

                #checks whether key is expired if expired that key value pair is deleted
                if(self.datastore[i]["timeout"] < time.time()):
                    print("Key '"+str(key)+"' expired!!!")
                    del self.datastore[i]
                else:
                    value = json.loads(self.datastore[i][key]) # converts json object to value
                    print("The value for the key '"+str(key)+"' is '"+str(value)+"'")
                return
            
        # if key is not found
        if(found == 0):
            print("No such key exists!!!")
            return

    def Delete(self,key):
        # deletes key-value pair from datastore

        #finds key in the datastore
        for i in self.datastore:
            if(key in self.datastore[i]):
                del self.datastore[i] #deletes key-value pair
                print("Deleted '"+str(key)+"' key-value pair successfully")
                return
            
        # if key is not found
        print("No such key exists!!!")
        return
        

    def print_datastore(self):
        for i in self.datastore:
            print(self.datastore[i])
        



    
